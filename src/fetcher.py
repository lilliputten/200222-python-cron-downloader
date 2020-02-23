# -*- coding:utf-8 -*-
# @module fetcher
# @since 2020.02.23, 18:51
# @changed 2020.02.23, 18:51


from logger import DEBUG
import loader
import parser


def fetchMatchesFromUrl(url):
    html = loader.loadHtml(url)
    matches = parser.fetchMatchesFromHtml(html)
    return matches


__all__ = [  # Exporting objects...
    'fetchMatchesFromUrl',
]

if __name__ == '__main__':  # Test
    url = 'https://echo.msk.ru/programs/radiodetaly/'
    matches = fetchMatchesFromUrl(url)
    DEBUG('fetcher: testing for fetchMatchesFromUrl', {'url': url, 'matches': matches})
