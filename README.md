# SPAMVID

## Purpose
To provide an easy way to create sub par *shitty meme comps!* Enjoy.

## Installation and setup
Install dependencies from `requirements.txt` and make sure ffmpeg is installed natively. Afterwards, correct the information in `config.py` and run it to create your configuration file. You can then run the script with the command `python spamvid.py`. Make sure you **DO NOT** host your `config.ini` or customized `config.py` file on a public server (i.e. github, gitlab, reddit, etc) as they may contain your secret key for the API.

## Usage
Run the script, if you set up your confiuration correctly you should be able to see a list of posts with their ratings after specifiying a subreddit and number of posts to scrape. The script will then work its magic, downloading both the audio tracks and video from the selected subreddit. It will then combine each respective track, and subsequently create a video from all combined tracks. 

### Extra tip
You may want to take from the hot or new sections instead of top. To do this, change `for post in subreddit.top(limit=howmany):` to `for post in subreddit.hot(limit=howmany):` or `for post in subreddit.new(limit=howmany):` respectively. An easier way to change this is in the works currently.


## DONT ROAST ME
It is a shitty project put together with love by the same people who made *[lottopy](https://github.com/lottopy/wvlottopy)*. Show them some appreciation. If you have any suggestions or want to contribute feel free to contact me via the email attached to the site linked above. 

### Thanks!