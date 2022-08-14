import os, logging, argparse
from pyfiglet import Figlet

parser = argparse.ArgumentParser()
parser.add_argument( '-log',
                     '--loglevel',
                     default='info',
                     )

args = parser.parse_args()

logging.basicConfig( level=args.loglevel.upper() )
logging.info('Starting setup, creating folders')

os.mkdir('./output')
os.mkdir('./audio')
os.mkdir('./videos')

f = Figlet(font='slant')
print(f.renderText('Welcome to SPAMVID'))
logging.info('Setup complete, please edit config.py and execute it')