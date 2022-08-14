import configparser
config = configparser.ConfigParser()
config['REDDIT'] = {'client_id': 'ENTER ID HERE', # ID 
    'client_secret': 'ENTER SECRET KEY HERE', #API Key
    'user_agent':'ENTER USER AGENT HERE (Could be anything)', # User Agent
    }
with open('config.ini', 'w') as configfile:
  config.write(configfile)

# This file is intended to make creating a configuation file easier. Run it once with the proper values and then run the bot. 