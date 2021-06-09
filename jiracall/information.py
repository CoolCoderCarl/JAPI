from jira import JIRA
from jiracall import settingsJ

# Jira authentication to SERVER by USERNAME and PASSWORD
options = {"server": settingsJ.servername}
jira = JIRA(options, basic_auth=(settingsJ.username, settingsJ.password))

# An ISSUE specify in the settings.ini
issue = jira.issue(settingsJ.tasknum)

def getInfo(issue):
    '''
    :param issue: task number like JIRA-1234
    :return:
    '''
    dscrp = issue.fields.description
    prjct = issue.fields.project
    cmmnt = issue.fields.comment

    summary = ( dscrp, prjct, cmmnt )

    print(summary)

def getWorklogs(issue):
    '''
    :param issue: task number like JIRA-1234
    :return:
    '''
    author = issue.fields.worklog.worklogs[0].author
    cmmnt = issue.fields.worklog.worklogs[0].comment
    cretd = issue.fields.worklog.worklogs[0].created
    strtd = issue.fields.worklog.worklogs[0].started
    tmSpnt = issue.fields.worklog.worklogs[0].timeSpent

    workSum = ( author, cmmnt, cretd, strtd, tmSpnt )

    print(workSum) # index out of range for some tasks
