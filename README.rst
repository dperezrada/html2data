.. -*- mode: rst; coding: utf-8 -*-

Welcome to Html2Data
====================

:Author: * Daniel Perez Rada <dperezrada@gmail.com>

Description
===========
A simple way to transform a HTML file or URL to structured data.  You only need to define the xpath to the element. Optionaly you can define functions to be applied after. You can easily write XPATH using the firebug extension, copy XPATH (I recommend edit the XPATH given by firebug, making it shorter).

Example
=======

::

	$ from html2data import HTML2Data
	$ url = "http://pypi.python.org/pypi/html2data"
	>> config = [{'name': 'author', 'xpath': '//ul[@class="nodot"]}

	>> h2d_instance = HTML2Data(html = html)
	>> print h2d_instance.parse_one(xpath = '//head/title/text()')
	'Example Page'

Requirement
===========

 * lxml 2.0+
 * httplib2

Tests
=====
Requirement
-----------

 * ludibrio
 * nose

Run
---

    >> nosetests
 