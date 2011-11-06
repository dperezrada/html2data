## Description ##
A simple way to transform a HTML file or URL to structured data.  You only need to define the xpath to the element. Optionaly you can define functions to be applied after. You can easily write XPATH using the firebug extension, copy XPATH (I recommend edit the XPATH given by firebug, making it shorter).

## Example ##
    >> from html2data import HTML2Data
    >> html = """<!DOCTYPE html><html lang="en"><head>
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

    >> h2d_instance = HTML2Data(html = html)
    >> print h2d_instance.parse_one(xpath = '//head/title/text()')
    'Example Page'

## Requirement ##

 * lxml 2.0+
 * httplib2

## Tests ##
### Requirement ###

 * ludibrio
 * nose

### Run ###

    >> nosetests
 