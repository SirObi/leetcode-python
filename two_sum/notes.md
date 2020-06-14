### Lessons learned:  
Do NOT use constructs like:  
```
if x:
    do something
```  

Prefer `if x == (some condition)`:  
```
if x is not None:
    do something  
```


Also, use `None` as default value for `dict.get()`, don't use `False`.  
