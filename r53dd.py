import updater
import ConfigParser
import os


scriptPath = os.path.dirname( __file__ )
stdConfigPath = '/etc/r53dd'
configFileName = 'updater.cfg'
configFilePath = None

if (os.access(scriptPath + os.sep + configFileName, os.R_OK)):
    configFilePath = scriptPath + os.sep + configFileName

if (os.access(stdConfigPath + os.sep + configFileName, os.R_OK)):
    configFilePath = stdConfigPath + os.sep + configFileName

if (configFilePath == None):
    exit('Config file missing.')

config = ConfigParser.RawConfigParser()
config.read('updater.cfg')

hosted_zone = config.get('settings', 'hosted_zone')
aws_key =  config.get('settings', 'aws_key')
aws_secret = config.get('settings', 'aws_secret')
ttl = config.get('settings', 'ttl')
hostname = config.get('settings', 'hostname')

if len(hostname) < 1:
    hostname = None

r53 = updater.r53dd(hosted_zone, aws_key, aws_secret, ttl, hostname)
r53.updateIp()

