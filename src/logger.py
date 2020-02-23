# -*- coding:utf-8 -*-
# @module logger
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:32


import os
from os import path
from config import config
import datetime
#  import pprint
import yaml
from termcolor import colored


def writeToLogFile(title, data):
    print 'Trying to write to file...'


def createHeader():
    detailedDateFormat = config['detailedDateFormat']
    now = datetime.datetime.now()
    dateTag = now.strftime(detailedDateFormat)
    header = '[' + dateTag + ']'
    return header


def createLogData(title, data=None):
    logData = ''
    if data is not None:
        logData = yaml.safe_dump(data)
        #  logData += pprint.pformat(data)
        if not logData.endswith('\n'):
            logData += '\n'
    return logData


loggedEntries = 0


def DEBUG(title, data=None):
    global loggedEntries
    header = createHeader()
    logData = createLogData(title, data)  # Ensure trailing newline for record delimiting
    fileMode = 'a'  # Default file mode: append
    if loggedEntries == 0:
        #  print '[Log started]\n'  # Insert empty line to stdout
        if config['clearLogFile']:
            fileMode = 'w'  # Clear file on first entry
    if config['writeLog']:
        rootPath = os.getcwd()
        logFile = path.join(rootPath, 'log.txt')
        with open(logFile, fileMode) as file:
            file.write(header + '\n')
            file.write(title + '\n')
            file.write(logData + '\n')
    if config['outputLog']:
        if config['outputColoredLog']:
            header = colored(header, 'green')
            title = colored(title, 'red')
        print header
        print title
        print logData
    loggedEntries += 1


__all__ = [  # Exporting objects...
    'DEBUG',
]
