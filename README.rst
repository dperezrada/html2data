.. -*- mode: rst; coding: utf-8 -*-

Welcome to Html2Data
====================

:Author: * Daniel Perez Rada <dperezrada@gmail.com>

Description
===========
A simple way to transform a HTML file or URL to structured data.  You only need to define the xpath to the element. Optionaly you can define functions to be applied after. You can easily write XPATH using the firebug extension, copy XPATH (I recommend edit the XPATH given by firebug, making it shorter).

Example
=======
Import
------
::

>>> from html2data import HTML2Data

Create instance
---------------
::

	>>> html = """<!DOCTYPE html><html lang="en"><head>
	    	<meta charset="utf-8" />
	    	<title>Example Page</title>
	    	<link rel="stylesheet" href="css/main.css" type="text/css" />
			</head>
			<body>
	    		<h1><b>Title</b></h1>
	    		<div class="description">This is not a valid HTML
			</body>
		</html>"""
	>>> h2d_instance = HTML2Data(html = html) #You can also create it from a url = url

Using XPATH config
--------------------
One you have the object 
::

	>>> config = [
            {'name': 'header_title', 'xpath': '//head/title/text()'},
            {'name': 'body_title', 'xpath': '//h1/b/text()'},
            {'name': 'description', 'xpath': '//div[@class="description"]/text()'},
        ]

	>>> h2d_instance.parse(config = config)
	{'header_title': 'Example Page', 'body_title': 'Title', 'description': 'This is not a valid HTML'}

Using CSS SELECTOR config
---------------------------
::

	>>> config = [
	        {'name': 'header_title', 'css': 'head title'},
	        {'name': 'body_title', 'css': 'h1 b '},
	        {'name': 'description', 'css': 'div.description'},
	    ]

	>>> h2d_instance.parse(config = config)
	{'header_title': 'Example Page', 'body_title': 'Title', 'description': 'This is not a valid HTML'}



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
 