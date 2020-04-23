# -*- coding:utf-8 -*-
# @module logger
# @since 2020.02.23, 02:18
# @changed 2020.04.23, 03:48


from os import path
import yaml

import utils

from config import config


class Channel:

    # default constructor
    def __init__(self, id):
        self.id = id
        rootPath = config['rootPath']
        channelsDir = config['channelsDir']
        fileName = id + '.yaml'
        self.filePath = path.join(rootPath, channelsDir, fileName)

    def __str__(self):
        return '<Channel:' + str(self.id) + '>'

    @staticmethod
    def yamlRepr(dumper, self):
        #  return dumper.represent_str('tag:yaml.org,2002:str', str(self), style='')
        return dumper.represent_str(str(self))

    def loadConfig(self):
        if path.isfile(self.filePath):
            with open(self.filePath) as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
                self.data = data

    def saveConfig(self):
        with open(self.filePath, 'w') as file:
            data = yaml.dump(self.data, Dumper=utils.CustomYamlDumper, default_flow_style=False, indent=2)
            file.write(data)


yaml.add_representer(Channel, Channel.yamlRepr)
