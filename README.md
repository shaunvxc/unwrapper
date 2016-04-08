# unwrap
:gift: Unwrap callback functions from JSON responses 

`unwrap` is a small utility for unwrapping the callback function from an otherwise easily parseable `json` string.

###Usage
Simply pass the in the string to be unwrapped:

```python
from unwrap import unwrap

print unwrap("json13123({'a':1, 'b': 2, 'c': 3})")
# this will output: {'a':1, 'b': 2, 'c': 3}
```

Once the callback is removed, the JSON can be be parsed into a much more useful format like so:

```python
import json
from unwrap import unwrap

data = json.loads(unwrap("json13123({'a':1, 'b': 2, 'c': 3})"))
```
