# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

from src import config, DEBUG

import urllib2
from os import path
import re

DEBUG('Started ' + __file__ + ' / ' + config['buildTag'])
DEBUG('Using config:', config)

response = urllib2.urlopen('https://echo.msk.ru/programs/radiodetaly/')
html = response.read()
matches = re.findall(r'\w+\.mp3', html)

with open(path.join(config['rootPath'], 'log-request.txt'), 'w') as file:
    file.write(html)

DEBUG('Test', {
    'matches': matches,
})
