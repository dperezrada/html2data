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
-------------------------
::

	>>> config = [
	        {'name': 'header_title', 'css': 'head title'},
	        {'name': 'body_title', 'css': 'h1 b '},
	        {'name': 'description', 'css': 'div.description'},
	    ]

	>>> h2d_instance.parse(config = config)
	{'header_title': 'Example Page', 'body_title': 'Title', 'description': 'This is not a valid HTML'}


Real life example
-----------------
::

	import urllib2

	from html2data import HTML2Data

	response = urllib2.urlopen('http://sil.senado.cl/cgi-bin/sil_ultproy.pl')
	html = response.read()

	config = [
	    {'name': 'fecha', 'css': 'td:nth-child(1)'},
	    {'name': 'id', 'css': 'td:nth-child(2) a'},
	    {'name': 'nombre', 'css': 'td:nth-child(3)'},
	    {'name': 'estado', 'css': 'td:nth-child(4)'},
	]

	html_instance = HTML2Data(html = html)
	rows = html_instance.parse_one(css = 'td td tr', multiple = True, text = False)
	for row_element in rows:
	    row_in_html = HTML2Data(tree = row_element)
	    print row_in_html.parse(config = config)

You will get something like:
::

	{'nombre': 'Reforma Constitucional que restablece obligatoriedad del voto.', 'fecha': '24/11/2011', 'estado': 'En tramitación', 'id': '8062-07'}
	..
	{'nombre': 'Prohíbe el anatocismo.', 'fecha': '02/11/2011', 'estado': 'En tramitación', 'id': '8007-03'}


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
 