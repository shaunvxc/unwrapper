#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

def unwrap(content):
    starting_symbol = get_start_symbol(content)
    ending_symbol = ']' if starting_symbol == '[' else '}'
    start = content.find(starting_symbol, 0)
    end = content.rfind(ending_symbol)
    return json.loads(content[start:end+1])


def get_start_symbol(content):
    if content.find('[') > 0 and content.find('[') < content.find('{'):
        return '['
    if content.find('{') > 0 and content.find('{') < content.find('['):
        return '{'

    print ("Unable to find start of JSON string")
    return "{"
