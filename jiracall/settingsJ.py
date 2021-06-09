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
server=https://jira.com
[task]
num=JIRA-1234''')
        file.close()

# Get settings from file
conf = configparser.ConfigParser()
conf.read('settings.ini')

username = conf['auth']['username'] # USERNAME of jira user
password = conf['auth']['password'] # PASSWORD
servername = conf['server']['server'] # JIRA SERVER
tasknum = conf['task']['num'] # TASK NUMBER

