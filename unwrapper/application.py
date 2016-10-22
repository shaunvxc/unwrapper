#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

class CannotFindJsonBoundaryError(Exception):
    def __init__(self):
        Exception.__init__(self, "Could not find valid start/ending JSON boundaries-- most likely invalid JSON")

def unwrap(content):
    """ unwraps the callback and loads the JSON into a dict
    """
    return json.loads(unwrap_raw(content))


def loads(content):
    """ for consistency with json package
    """
    return json.loads(unwrap_raw(content))


def unwrap_raw(content):
    """ unwraps the callback and returns the raw content
    """
    starting_symbol = get_start_symbol(content)
    ending_symbol = ']' if starting_symbol == '[' else '}'
    start = content.find(starting_symbol, 0)
    end = content.rfind(ending_symbol)
    return content[start:end+1]

def get_start_symbol(content):
    if content.find('[') > 0 and content.find('[') < content.find('{'):
        return '['

    if content.find('{') > 0:
        return '{'
    # if we cannot find these symbols, we raise a CannotFindBoundaryError--
    # note that it is entirely possible for this TO NOT happen EVEN IF non-json
    # is passed to the package..
    raise CannotFindJsonBoundaryError()
