#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module created for downloading topics from portal"""
import urllib
import json

url = "https://www.reddit.com/r/python.json"
response = urllib.urlopen(url)
data_json = json.loads(response.read())


def red_dit():
    """Main function"""

    def inner_func(data):
        """Returns new topic from the list of topics"""
        yield outer_function(data)

    return inner_func


container = []


def outer_function(data):
    """Performs search in the JSON"""
    global container
    for element in data:
        if element == u'title':
            container.append(data[element])
        if isinstance(element, (list, dict)):
            outer_function(element)
        if isinstance(data, dict) and isinstance(data[element], (list, dict)):
            outer_function(data[element])
    return container


red21 = red_dit()
var = red21(data_json).next()
for title in var:
    print (title)
