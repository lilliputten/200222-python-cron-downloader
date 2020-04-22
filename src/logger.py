# -*- coding:utf-8 -*-
# @module logger
# @since 2020.02.23, 02:18
# @changed 2020.04.22, 01:38


import os
from os import path
from config import config
import datetime
import yaml
from termcolor import colored
import utils  # noqa


def createHeader():
    detailedDateFormat = config['detailedDateFormat']
    now = datetime.datetime.now()
    dateTag = now.strftime(detailedDateFormat)
    #  if dateTag.endswith('000'):  # Remove extra finsishing '000'
    dateTag = dateTag[:-3]  # Convert microseconds (.NNNNNN) to milliseconds (.NNN)
    header = '[' + dateTag + ']'
    return header


def createLogData(title, data=None):
    logData = ''
    if data is not None:
        #  logData = yaml.dump(data, default_flow_style=False)
        logData = yaml.dump(data)
        #  logData += pprint.pformat(data)
        if not logData.endswith('\n'):
            logData += '\n'
        #  if 'test' in data:
        #      print 'Test data:', data
        #      print 'Test yaml:', logData
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

if __name__ == '__main__':  # Test
    DEBUG('Test')
