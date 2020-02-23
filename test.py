# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

from src import config, DEBUG
#  import sys

#  print 'config:', config
DEBUG('Started ' + __file__ + ' / ' + config['buildTag'])
DEBUG('Using config:', config)
DEBUG('Test', {'a': True})

#  print server.rootPath
