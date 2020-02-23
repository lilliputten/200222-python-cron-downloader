# -*- coding:utf-8 -*-
# @module loader
# @since 2020.02.23, 18:46
# @changed 2020.02.23, 18:53


import urllib2
from logger import DEBUG


def loadHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


__all__ = [  # Exporting objects...
    'loadHtml',
]

if __name__ == '__main__':  # Test
    #  url = 'https://echo.msk.ru/programs/radiodetaly/'
    url = 'http://www.example.com/'
    DEBUG('Testing for url', {'url': url})
    html = loadHtml(url)
    DEBUG('loaded html', {'url': url, 'html': html})
