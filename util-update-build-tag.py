# -*- coding:utf-8 -*-
# @module util-update-build-tag
# @since 2020.02.23, 00:58
# @changed 2020.02.23, 01:58

import json
import datetime

buildTagFile = 'build-tag.txt'

dateTagFormat = '%y%m%d-%H%M'
shortDateFormat = '%Y.%m.%d-%H:%M'
detailedDateFormat = shortDateFormat + ':%S.%f'

now = datetime.datetime.now()
dateTag = now.strftime(dateTagFormat)

pkgConfig = json.load(open('package.json'))
version = pkgConfig['version']

buildTag = 'v.' + version + '-' + dateTag

print buildTag

with open(buildTagFile, 'w') as f:
    f.write(buildTag)
