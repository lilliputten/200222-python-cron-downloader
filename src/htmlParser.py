# -*- coding:utf-8 -*-
# @module htmlParser
# @since 2020.02.23, 14:25
# @changed 2020.02.23, 18:13


from os import path
from logger import DEBUG
import re


def fetchMatchesFromHtml(html):
    matches = re.findall(r'href="([^"]*\.mp3)"', html)
    #  DEBUG('htmlParser:fetchMatchesFromHtml: found matches', {
    #      'matches': matches,
    #  })
    return matches


__all__ = [  # Exporting objects...
    'fetchMatchesFromHtml',
]

if __name__ == '__main__':  # Test
    modulePath = path.dirname(path.abspath(__file__))
    testFileName = 'parser-test-radiodetaly-fragment.html'
    testFilePath = path.join(modulePath, testFileName)
    print 'Testing with', testFilePath
    with open(testFilePath) as file:
        html = file.read()
        matches = fetchMatchesFromHtml(html)
        DEBUG('htmlParser:test:fetchMatchesFromHtml: found matches', {
            'matches': matches,
        })
