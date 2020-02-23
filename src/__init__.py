# -*- coding:utf-8 -*-
# @module server:init
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 01:58

#  import os
#  rootPath = os.getcwd()

from config import config
from logger import DEBUG

from main import foo  # noqa

__all__ = [
    'config',
    'DEBUG',
]

#  print 'config: ', config
#  foo()
