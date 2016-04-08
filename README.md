# unwrap [![Build Status](https://travis-ci.org/shaunvxc/unwrap.svg?branch=master)](https://travis-ci.org/shaunvxc/unwrap) [![PyPI version](https://badge.fury.io/py/unwrapper.svg)](https://badge.fury.io/py/unwrapper)

`unwrapper` is a small utility for unwrapping the callback function from an otherwise easily parseable `json` string.

###Usage
Simply pass the in the string to be unwrapped:

```python
from unwrapper import unwrap

x = unwrap("json13123({'a':1, 'b': 2, 'c': 3})")
# x is {u'a': 1, u'c': 3, u'b': 2}
```

And you will get back a parsed json dictionary.
 
####Command Line
 
 `$ curl "SOME CURL REQUEST RETURNING WRAPPED JSON" | unwrap`
 
###Installation

`$ pip install unwrapper`
