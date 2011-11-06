# encoding: utf-8
import os
from unittest import TestCase


from html2data import HTML2Data

def getOne(elements):
    if len(elements) >0:
        return elements[0]
    return None


class TestParse(TestCase):
    def setUp(self):
        html = """<!DOCTYPE html><html lang="en"><head>
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
        self.html2data_instance = HTML2Data(html = html)

    def test_xpath(self):
        title = self.html2data_instance.xpath('//head/title/text()')
        self.assertEqual(['Example Page',], title)
    
    def test_parse_one_element(self):
        dict_parsed = self.html2data_instance.parse_one(xpath = '//ul[@id="some_cities"]/li', multiple = True)
        expected_array = ['Santiago', 'Valparaiso']
        self.assertEqual(expected_array, dict_parsed)
    
    def test_parse_with_xpath_config(self):
        config = [
            {'name': 'title',  'xpath': '//head/title'},
            {'name': 'body_title',  'xpath': '//h1/b'},
            {'name': 'description',  'xpath': '//div[@class="description"]', 'strip': False},
            {'name': 'cities',  'xpath': '//ul[@id="some_cities"]/li', 'multiple': True},
        ]
        dict_parsed = self.html2data_instance.parse(config)
        expected_dict = {
            'title': 'Example Page',
            'body_title': 'Title',
            'description': 'This is not a valid XML\n                ',
            'cities': [
                'Santiago',
                'Valparaiso',
            ]
        }
        self.assertEqual(expected_dict, dict_parsed)