#!python2
# -*- coding:utf-8 -*-
# @module test
# @since 2020.02.23, 02:18
# @changed 2020.02.23, 03:04

#  from src import config
from src import DEBUG
from src.Channel import Channel


def run():
    id = 'echo-radiodetaly'
    DEBUG('Start creating channel: ' + id)
    channel = Channel(id)
    channel.loadConfig()
    DEBUG('Channel ' + id + ' created', {
        'channel': channel,
    })
    channel.saveConfig()
