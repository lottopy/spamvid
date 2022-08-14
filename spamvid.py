import re, os, glob, praw, urllib.request, configparser
import ffmpeg as ff

def concatenate():
	begin = "ffmpeg -i \"concat:"
	fin_video = glob.glob("*.mp4")
	file_temp = []
	for f in fin_video:
		file = "temp" + str(fin_video.index(f) + 1) + ".ts"
		os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
		file_temp.append(file)
	print(file_temp)
	for f in file_temp:
		begin += f
		if file_temp.index(f) != len(file_temp)-1:
			begin += "|"
		else:
			begin += "\" -c copy  -bsf:a aac_adtstoasc final.mp4"
	print(begin)
	os.system(begin)

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config.get('REDDIT', 'client_id')
client_secret = config.get('REDDIT', 'client_secret')
user_agent = config.get('REDDIT', 'user_agent')

reddit = praw.Reddit(
    client_id=client_id, # ID 
    client_secret=client_secret, #API Key
    user_agent=user_agent, # User Agent
    )

subreddit = reddit.subreddit(input("Enter subreddit (no 'r/' necessary): ")) # Subreddit to search
howmany = int(input("How many posts to download? "))

posts = []
for post in subreddit.top(limit=howmany):
    try:
        print(F"Title: {post.title} \n Score: {post.score} Comments: {post.num_comments} \n URL: {post.url} \n {post.media['reddit_video']['fallback_url']} \n" 
        F"---------------------------------------------------------------------------------------------------------------------")
        posts.append(post.media['reddit_video']['fallback_url'])
    except (TypeError): 
        print(F'Post is missing title or something idrc, skipping it')
        pass

audio_posts = []
for post in list(posts):
    #print(post)
    audio_posts.append(re.sub(r'DASH_\d{3}.*', 'DASH_audio.mp4', post))
    
dir = os.getcwd()
os.chdir(dir+'/videos')
for post in posts:
    filename = post.split('/')[-2] + '.mp4'
    try:
        if not os.path.exists(filename):
            urllib.request.urlretrieve(post, filename)
        else: print(F"{filename} already exists")
    except:
        print("HTTP Error 403: Forbidden")
        continue

os.chdir(dir+'/audio')
for post in audio_posts:
    filename = post.split('/')[-2] + '_audio.mp4'
    try:
        if not os.path.exists(filename):
            urllib.request.urlretrieve(post, filename)
        else: print(F"{filename} already exists")
    except:
        print("HTTP Error 403: Forbidden")
        continue 

os.chdir(dir+'/output')

try:
    for audio in os.listdir(dir+'/audio'):
        filename = audio.split('_audio')[0] + '.mp4'
        for file in os.listdir(dir+'/videos'):
            if filename == file:
                audio = ff.input(dir+'/audio/'+filename.split('.')[0]+'_audio.mp4') #.audio.filter('adelay', "1|1")
                video = ff.input(dir+'/videos/'+filename)
                #adj_audio = ff.filter([audio], 'amix')
                ff.concat(video, audio, a=1, v=1).output(filename).run()
                print(F"{filename} created")
            else: pass
except (FileNotFoundError, PermissionError):
    print("Matching audio not found, skipping")
    pass
 
concatenate() # Concatenate videos in output folder

def clean():
    for file in os.listdir(dir+'/output'):
        if file != 'final.mp4':
            os.remove(dir+'/output/'+file)
        else:
            pass
    for file in os.listdir(dir+'/audio'):
        os.remove(dir+'/audio/'+file)
    for file in os.listdir(dir+'/videos'):
        os.remove(dir+'/videos/'+file)
    print("Cleanup complete")
    
clean()