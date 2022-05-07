
# sfuzzie
sfuzzie is a simple fuzz tree algorithem, provide fuzzing for words

## example

```py
from sfuzzie import fuzz

fuzzer = fuzz([
    "hello world",
    "fuzzing",
    "fuling"
])

print(fuzzer.suggest("hel fu w"))
```

### output:
```
[['hello'], ['fuzzing', 'fuling'], ['world']]
```

## install
```
python3 -m pip3 install sfuzzie
```
