# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

from server import config, DEBUG


#  print 'config:', config
DEBUG('Started ' + config['buildTag'])
DEBUG('Started with config:', config)

#  print server.rootPath
