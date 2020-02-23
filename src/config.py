# -*- coding:utf-8 -*-
# @module server
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 01:58
# See https://docs.python.org/3/library/configparser.html -- ???

import os
from os import path
import json
import yaml

rootPath = os.getcwd()
yamlConfigFilename = path.join(rootPath, 'config.yml')

buildTagFilename = path.join(rootPath, 'build-tag.txt')
packageFilename = path.join(rootPath, 'package.json')
#  print 'config: packageFilename', packageFilename  # DEBUG

version = 'Testing'
buildTag = 'Testing'

if path.isfile(packageFilename):
    pkgConfigFile = open(packageFilename)
    pkgConfig = json.load(pkgConfigFile)
    version = pkgConfig['version']
    pkgConfigFile.close()

if path.isfile(buildTagFilename):
    buildTagFile = open(buildTagFilename, 'r')
    buildTag = buildTagFile.read()
    buildTagFile.close()

config = {  # Default config
    'version': version,
    'buildTag': buildTag,
    'rootPath': rootPath,
    'outputLog': True,
    'outputColoredLog': True,
    'writeLog': True,
    'clearLogFile': True,
    'dateTagFormat': '%y%m%d-%H%M',
    'shortDateFormat': '%Y.%m.%d-%H:%M',
    'detailedDateFormat': '%Y.%m.%d-%H:%M:%S.%f',
    'collectorFileName': 'collector.txt',  # Add to gitignore
}

# Extend config from file (config.yml) in project root
if path.isfile(yamlConfigFilename):
    with open(yamlConfigFilename) as file:
        #  print 'Extending config with', yamlConfigFilename
        yamlConfigData = yaml.load(file, Loader=yaml.FullLoader)
        #  print 'yamlConfigData:', yamlConfigData
        config.update(yamlConfigData)
