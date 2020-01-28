import os
import configparser

# create setting file if not exist
def createSettingsFile():
    if not os.path.exists('settings.ini'):
        file = open('settings.ini', 'w+')
        file.write(
'''[auth]
username=admin
password=admin
[server]
server=https://jira.com''')
        file.close()

# get settings from file

conf = configparser.ConfigParser()
conf.read('settings.ini')

username = conf['auth']['username']
password = conf['auth']['password']

servername = conf['server']['server']

