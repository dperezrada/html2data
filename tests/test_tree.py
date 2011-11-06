# encoding: utf-8
import os
from unittest import TestCase

from httplib2 import Http
from ludibrio import Mock

from html2data import HTML2Data

class TestTree(TestCase):
    def setUp(self):
        self.html = """<!DOCTYPE html><html lang="en"><head>
                <meta charset="utf-8" />
                <title>Example Page</title>
                <link rel="stylesheet" href="css/main.css" type="text/css" />
            </head>
            <body>
                <h1><b>Title</b></h1>
                <div class="description">This is not a valid XML
                <ul id="some_cities">Cities 
                    <li>Santiago</li>
                    <li>Valparaiso</li>
                </ul>
            </body>
        </html>"""
        self.url = 'https://github.com/dperezrada'

    def test_parse_title_from_html(self):
        html2data_instance = HTML2Data(html = self.html)
        title = html2data_instance.xpath('//head/title/text()')
        self.assertEqual(['Example Page',], title)
    
    def test_parse_title_from_url(self):
        with Mock() as Http:
            from httplib2 import Http
            connection = Http()
            connection.request(self.url) >> ({'headers': ''}, self.html)
        html2data_instance = HTML2Data(url = self.url)
        title = html2data_instance.xpath('//head/title/text()')
        self.assertEqual(['Example Page',], title)
        