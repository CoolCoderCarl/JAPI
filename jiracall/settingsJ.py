import os
import configparser

### Create setting file if not exist
def createSettingsFile():
    if not os.path.exists('settings.ini'):
        file = open('settings.ini', 'w+')
        file.write(
'''[auth]
username=admin
password=admin
[server]
server=https://jira.com
[task]
num=JIRA-1234''')
        file.close()

### Get settings from file
conf = configparser.ConfigParser()
conf.read('settings.ini')

username = conf['auth']['username'] # Username of jira user
password = conf['auth']['password'] # Password
servername = conf['server']['server'] # Jira servername
tasknum = conf['task']['num'] # Task number

