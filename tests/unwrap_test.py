# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sure

import unwrap


def test_basic_unwrap():
    unwrap.unwrap("json13123({'a':1, 'b': 2, 'c': 3})").should.equal("{'a':1, 'b': 2, 'c': 3}")


def test_unwrap_list():
    unwrap.unwrap("json13123([{'a':1, 'b': 2, 'c': 3}, {'d':1, 'e': 2, 'f': 3}])").should.equal("[{'a':1, 'b': 2, 'c': 3}, {'d':1, 'e': 2, 'f': 3}]")


# if __name__ == '__main__':
#     test_basic_unwrap()
