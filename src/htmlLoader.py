# -*- coding:utf-8 -*-
# @module htmlLoader
# @since 2020.02.23, 18:46
# @changed 2020.04.22, 05:25


import urllib2
from logger import DEBUG
import errors
import utils
#  import http.client


def loadHtml(url):
    try:
        DEBUG('htmlLoader: request start', {
            'url': url
        })
        response = urllib2.urlopen(url)
        responseDict = utils.dictFromClass(response)
        DEBUG('htmlLoader: request successful', {
            'url': url,
            'status': '{code} ({msg})'.format(**responseDict),
            'content-length': int(response.headers.dict['content-length']),
            'type': response.headers.type,
        })
        data = response.read()
        DEBUG('htmlLoader: data readed', {
            'url': url,
            #  'data': utils.BlockString(data, 500),
            'data': utils.truncateLongString(data, 600),
        })
        return data
    except Exception, error:
        DEBUG('htmlLoader: error catched', {
            'url': url,
            'error': errors.toBlockString(error),
        })


__all__ = [  # Exporting objects...
    'loadHtml',
]

if __name__ == '__main__':  # Test
    #  url = 'https://echo.msk.ru/programs/radiodetaly/'
    url = 'http://www.example.com/'
    DEBUG('Testing for url', {'url': url})
    html = loadHtml(url)
    if html:
        DEBUG('loaded html', {
            'url': url,
            'html': utils.BlockString(html, 300),
        })
