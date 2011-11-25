# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(fname):
    print os.path.join(os.path.dirname(__file__), fname)
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "html2data",
    version = "0.4.2",
    author = "Daniel Perez Rada",
    author_email = "dperezrada@gmail.com",
    description = ("A simple way to transform a HTML file or URL to structured data."),
    license = "BSD",
    keywords = "html2data html data xpath crawler transform",
    url = "https://github.com/dperezrada/html2data",
    packages=['html2data', 'tests'],
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
      "lxml>=2.0.0","httplib2"
    ],
)
