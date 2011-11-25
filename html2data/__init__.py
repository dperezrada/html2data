# -*- coding: utf-8 -*-
from lxml import etree
from StringIO import StringIO
from copy import copy

from httplib2 import Http

class HTML2Data(object):
    def __init__(self, html = None, url = None, tree = None):
        if not (html or url or tree):
            raise Exception('html or url or tree parameters are required')
        if url:
            connection = Http()
            header, html = connection.request(url)
        elif html:
            self.tree = self._get_tree_from_html(html)
        else:
            self.tree = tree
        
    @staticmethod
    def _get_tree_from_html(html):
        parser = etree.HTMLParser()
        return etree.fromstring(html, parser)
    
    def xpath(self, expression):
        return self.tree.xpath(expression)
    
    def css_select(self, expression, text = False):
        from lxml.cssselect import CSSSelector
        sel = CSSSelector(expression)
        selected_elements = sel(self.tree)
        if text:
            selected_elements = map(lambda x: x.text, selected_elements)
        return selected_elements

    @staticmethod
    def _check_config(element):
        if not isinstance(element, dict):
            raise Exception('Each element in the config list, must be an dict')
        elif not element.get('name'):
            raise Exception('Each element must have the key "name"')
        elif not (element.get('xpath') or element.get('css')):
            raise Exception('Each element must have the key "xpath" or "css"')
    
    @staticmethod
    def _get_text(elements):
        return map(lambda x: x.text, elements)

    @staticmethod
    def _strip(elements):
        return map(lambda x: str.strip(x.encode('utf-8')), elements)

    @staticmethod
    def _get_one(elements):
        return (elements or [None])[0]

    def _apply_after(self, value, apply_after, multiple, strip, text):
        total_added_after = 0
        if not multiple:
            apply_after.insert(0,  self._get_one)
        if strip and text:
            apply_after.insert(0,  self._strip)
        if text:
            apply_after.insert(0,  self._get_text)
        for after in apply_after:
            value = after(value)
        return value
            
    def parse_one(self, xpath = None, css = None, multiple = False, apply_after = [], text = True, strip = True):
        #TODO: Be able to return elements and text
        if xpath:
            value = self.xpath(xpath.replace('/text()', ''))
        elif css:
            value = self.css_select(css)
        value = self._apply_after(value, copy(apply_after), multiple, strip, text = text)
        return value
        
    def parse(self, config):
        parsed_dict = {}
        for element in config:
            self._check_config(element)
            value = self.parse_one(
                xpath = element.get('xpath'), 
                css = element.get('css'),
                multiple = element.get('multiple', False),
                apply_after = element.get('apply_after', []),
                strip = element.get('strip', True)
            )
            parsed_dict[element.get('name')] = value
        return parsed_dict