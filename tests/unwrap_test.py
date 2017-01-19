# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sure
import json

from unwrapper import unwrap, unwrap_raw, loads, CannotFindJsonBoundaryError


def test_basic_unwrap():
    # z = unwrap(u'null({"result":ERROR})')
    unwrap('json13123({"a":1, "b": 2, "c": 3})').should.equal(json.loads('{"a":1, "b": 2, "c": 3}'))


def test_loads():
    loads('json13123({"a":1, "b": 2, "c": 3})').should.equal(json.loads('{"a":1, "b": 2, "c": 3}'))


def test_unwrap_list():
    unwrap('json13123([{"a":1, "b": 2, "c": 3}, {"d":1, "e": 2, "f": 3}])').should.equal(json.loads('[{"a":1, "b": 2, "c": 3}, {"d":1, "e": 2, "f": 3}]'))
    x = unwrap('json13123([{"a":1, "b": 2, "c": 3}, {"d":1, "e": 2, "f": 3}])')
    assert x[0]["a"] == 1


def test_unwrap_raw():
    unwrap_raw('json13123([{"a":1, "b": 2, "c": 3}, {"d":1, "e": 2, "f": 3}])').should.equal('[{"a":1, "b": 2, "c": 3}, {"d":1, "e": 2, "f": 3}]')


def test_unwrap_invalid_inputs():
    unwrap.when.called_with('<html>....</html>').should.throw(CannotFindJsonBoundaryError)
