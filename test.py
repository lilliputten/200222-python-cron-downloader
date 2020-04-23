#!python2
# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

from src import config, DEBUG

#  import testLoad as test
import testChannel as test


DEBUG('Started ' + __file__ + ' / ' + config['buildTag'])
DEBUG('Using config:', config)

test.run()
