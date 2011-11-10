# -*- coding: utf-8 -*-
from lxml import etree
from StringIO import StringIO
from copy import copy

from httplib2 import Http

class HTML2Data(object):
    def __init__(self, html = None, url = None):
        if not (html or url):
            raise Exception('html or url parameters are required')
        if url:
            connection = Http()
            header, html = connection.request(url)
        self.tree = self._get_tree_from_html(html)
        
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
        if not (isinstance(element, dict) and element.get('name') and (element.get('xpath') or element.get('css'))):
            raise Exception('invalid config: type must be dict, name and xpath keys are required')
    
    @staticmethod
    def _get_text(elements):
        return map(lambda x: x.text, elements)

    @staticmethod
    def _strip(elements):
        return map(lambda x: str.strip(x), elements)

    @staticmethod
    def _get_one(elements):
        return (elements or [None])[0]

    def _apply_after(self, value, apply_after, multiple, strip):
        total_added_after = 0
        if not multiple:
            apply_after.insert(0,  self._get_one)
        if strip:
            apply_after.insert(0,  self._strip)
        apply_after.insert(0,  self._get_text)
        for after in apply_after:
            value = after(value)
        return value
            
    def parse_one(self, xpath = None, css = None, multiple = False, apply_after = [], strip = True):
        #TODO: Be able to return elements and text
        if xpath:
            value = self.xpath(xpath.replace('/text()', ''))
        elif css:
            print "AAAAAAAAAA", css
            value = self.css_select(css)
        value = self._apply_after(value, copy(apply_after), multiple, strip)
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