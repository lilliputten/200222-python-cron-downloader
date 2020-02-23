# -*- coding:utf-8 -*-
# @module logger
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:32

import os
from os import path
from config import config
import datetime
import yaml
#  import pprint


rootPath = os.getcwd()
logFile = path.join(rootPath, 'log.txt')

loggedEntries = 0


def writeToLogFile(title, data):
    print 'Trying to write to file...'


def createHeader():
    detailedDateFormat = config['detailedDateFormat']
    now = datetime.datetime.now()
    dateTag = now.strftime(detailedDateFormat)
    header = '[' + dateTag + ']'
    return header


def createLogData(title, data=None):
    logData = createHeader() + '\n' + title + '\n'
    if data is not None:
        logData += yaml.safe_dump(data)
    return logData


def DEBUG(title, data=None):
    global loggedEntries
    logData = createLogData(title, data)
    fileMode = 'a'  # Derfault file mode: append
    if loggedEntries == 0:
        #  print '[Log started]\n'  # Insert empty line to stdout
        if config['clearLogFile']:
            fileMode = 'w'  # Clear file on first entry
    if config['outputLog']:
        print logData
    if config['writeLog']:
        with open(logFile, fileMode) as file:
            file.write(logData + '\n')
    loggedEntries += 1


__all__ = [
    'DEBUG',
]
