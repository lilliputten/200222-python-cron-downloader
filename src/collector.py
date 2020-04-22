#!python2
# -*- coding:utf-8 -*-
# @module collector
# @since 2020.02.23, 18:51
# @changed 2020.02.23, 18:51


from config import config
from logger import DEBUG
from os import path
import re


testing = False  # Testing mode, see __main__ module section below


def addNewUrlsToFile(collectorFilePath, urls):
    #  global testing
    try:
        isFileExists = path.isfile(collectorFilePath)
        fileMode = 'r+' if isFileExists else 'w'
        file = open(collectorFilePath, fileMode)
        if isFileExists:
            for line in file:
                #  DEBUG('collector:addNewUrlsToFile: readed line', {'line': line})
                urlLookup = re.search(r'^\S+ \S+ (.*)$', line)
                if urlLookup:
                    url = urlLookup.group(1)
                    if url in urls:  # If found url exists in new urls list
                        urls.remove(url)  # Remove url from new urls
                        #  if testing:
                        #      DEBUG('collector:addNewUrlsToFile: found exists url: ' + url)
            #  if testing:
            #      DEBUG('collector:addNewUrlsToFile: done', {
            #          'remaining (new) urls': urls,
            #      })
        if len(urls):
            for url in urls:
                #  if testing:
                #      DEBUG('collector:addNewUrlsToFile: add new url: ' + url)
                file.write('. NEW ' + url + '\n')
        file.close()
    finally:
        pass


def addNewUrls(urls):
    global testing
    rootPath = config['rootPath']
    collectorFileName = config['collectorFileName'] if not testing else 'collector-test.txt'
    collectorFilePath = path.join(rootPath, collectorFileName)
    if testing:
        DEBUG('collector: testing for addNewUrls', {
            'testing': testing,
            'collectorFilePath': collectorFilePath,
        })
    return addNewUrlsToFile(collectorFilePath, urls)


__all__ = [  # Exporting objects...
    'addNewUrls',
]

if __name__ == '__main__':  # Test
    testing = True  # global testing
    # Example test command (in /src):
    #  cp collector-test-orig.txt collector-test.txt && py collector.py && cat collector-test.txt
    addNewUrls([
        'newUrl',
        'existsUrl',
        'YYY',
    ])

# EOF
