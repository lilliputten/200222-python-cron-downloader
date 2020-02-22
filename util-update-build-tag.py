# -*- coding:utf-8 -*-
# @module util-update-build-tag
# @since 2020.02.23, 00:58
# @changed 2020.02.23, 01:58

import json
import datetime
import os
from os import path


rootPath = os.getcwd()

buildTagFile = path.join(rootPath, 'build-tag.txt')
packageFile = path.join(rootPath, 'package.json')

dateTagFormat = '%y%m%d-%H%M'
#  shortDateFormat = '%Y.%m.%d-%H:%M'
#  detailedDateFormat = shortDateFormat + ':%S.%f'

now = datetime.datetime.now()
dateTag = now.strftime(dateTagFormat)

pkgConfig = json.load(open(packageFile))
version = pkgConfig['version']

buildTag = 'v.' + version + '-' + dateTag

print 'Updated build tag:', buildTag

with open(buildTagFile, 'w') as f:
    f.write(buildTag)
