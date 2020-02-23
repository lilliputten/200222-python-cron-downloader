# -*- coding:utf-8 -*-
# @module server
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 01:58

import os
from os import path
import json
import yaml

rootPath = os.getcwd()
yamlConfigFilename = path.join(rootPath, 'config.yml')

buildTagFilename = path.join(rootPath, 'build-tag.txt')
packageFilename = path.join(rootPath, 'package.json')

pkgConfigFile = open(packageFilename)
pkgConfig = json.load(pkgConfigFile)
version = pkgConfig['version']
pkgConfigFile.close()

buildTagFile = open(buildTagFilename, 'r')
buildTag = buildTagFile.read()
buildTagFile.close()

config = {
    'version': version,
    'buildTag': buildTag,
    'rootPath': rootPath,
    #  'test': 'basic',
    #  'testDict': {
    #      'var': 'var content',
    #  },
    'outputLog': True,
    'writeLog': True,
    'clearLogFile': True,
    'dateTagFormat': '%y%m%d-%H%M',
    'shortDateFormat': '%Y.%m.%d-%H:%M',
    'detailedDateFormat': '%Y.%m.%d-%H:%M:%S.%f',
}

# Extend config from file (config.yml) in project root
if path.isfile(yamlConfigFilename):
    with open(yamlConfigFilename) as file:
        #  print 'Extending config with', yamlConfigFilename
        yamlConfigData = yaml.load(file, Loader=yaml.FullLoader)
        #  print 'yamlConfigData:', yamlConfigData
        config.update(yamlConfigData)
