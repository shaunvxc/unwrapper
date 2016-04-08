# unwrap
:gift: Unwrap callback functions from JSON responses 

`unwrapper` is a small utility for unwrapping the callback function from an otherwise easily parseable `json` string.

###Usage
Simply pass the in the string to be unwrapped:

```python
from unwrapper import unwrap

print unwrap("json13123({'a':1, 'b': 2, 'c': 3})")
# this will output: {'a':1, 'b': 2, 'c': 3}
```

Once the callback is removed, the JSON can be be parsed into a much more useful format like so:

```python
import json
from unwrapper import unwrap

data = json.loads(unwrap("json13123({'a':1, 'b': 2, 'c': 3})"))
print data['b'] # prints 2
```
 
####Command Line
 
 `$ curl "SOME CURL REQUEST RETURNING WRAPPED JSON" | unwrap`
 
 
