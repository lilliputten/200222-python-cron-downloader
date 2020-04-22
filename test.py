#!python2
# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

from src import fetcher, config, DEBUG

DEBUG('Started ' + __file__ + ' / ' + config['buildTag'])
DEBUG('Using config:', config)

testUrl = 'https://zzzecho.msk.ru/programs/radiodetaly/'

# Test fetcher...
matches = fetcher.fetchMatchesFromUrl(testUrl)

#  # Raw download test...
#  import urllib2
#  from os import path
#  import re
#  response = urllib2.urlopen(testUrl)
#  html = response.read()
#  matches = re.findall(r'\w+\.mp3', html)
#  # DEBUG: Request logging
#  with open(path.join(config['rootPath'], 'log-request.txt'), 'w') as file:
#      file.write(html)

DEBUG('Test', {
    'matches': matches,
})
