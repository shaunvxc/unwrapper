# unwrap [![Build Status](https://travis-ci.org/shaunvxc/unwrap.svg?branch=master)](https://travis-ci.org/shaunvxc/unwrap) [![PyPI version](https://badge.fury.io/py/unwrapper.svg)](https://badge.fury.io/py/unwrapper)

`unwrapper` is a small utility for unwrapping the callback function from an otherwise easily parseable `json` string.

###Usage
Simply pass the in the string to be unwrapped:
* To unwrap the `JSON` from a callback function, and obtain a parsed dictionary:
```python
from unwrapper import unwrap
unwrap('json13123({"a":1, "b": 2, "c": 3})') # returns this dict: {u'a': 1, u'c': 3, u'b': 2}
```
* To simply unwrap the callback wrapper, use `unwrap_raw`:
```python
from unwrapper import unwrap_raw
unwrap_raw('json13123({"a":1, "b": 2, "c": 3})') # returns '{"a":1, "b": 2, "c": 3}'
```

####Command Line
 
 `$ curl "SOME CURL REQUEST RETURNING WRAPPED JSON" | unwrap`
 
###Installation

`$ pip install unwrapper`
