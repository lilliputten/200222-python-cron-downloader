# -*- coding:utf-8 -*-
# @module logger
# @since 2020.02.23, 02:18
# @changed 2020.04.22, 01:38


import yaml
import re


def dictFromClass(cls):
    return dict(
        (key, value)
        for (key, value) in cls.__dict__.items()
        #  if key not in _excluded_keys
    )


# Yaml extending (TODO: Extract to separated module)...
# See:
# - https://www.programcreek.com/python/example/104725/yaml.add_representer


def truncateLongString(s, maxLength=0):
    if maxLength and len(s) >= maxLength:
        s = s[0:maxLength-3] + '...'
    return s


def prepareLongString(s, maxLength=0):
    s = re.sub(r'\s+\n', '\n', s)
    return truncateLongString(s, maxLength)


def yamlReprStr(dumper, data):
    if ('\n' in data or '\r' in data):  # Block style for long multiline strings...
        useStyle = '|' if len(data) > 30 else '"'
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style=useStyle)
    else:
        return dumper.represent_str(data)
        #  return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='\'')


yaml.add_representer(str, yamlReprStr)


class BlockString:

    # default constructor
    def __init__(self, string, maxLength=0):
        self.string = string
        self.maxLength = maxLength

    def prepareString(self):
        return prepareLongString(self.string, self.maxLength)


def reprBlockString(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data.prepareString(), style='|')


yaml.add_representer(BlockString, reprBlockString)

