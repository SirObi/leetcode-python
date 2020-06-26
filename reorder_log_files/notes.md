## Summary

When you hear `sorting`, think `keys`.
Read instructions carefully.

## Code

Solution 1 - failing for logs which don't start with 'let' or 'dig'  
Lessons learned:  
read the instructions carefully - create some inputs by hand and clarify if
they match the description.  

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) <= 1:
            return logs

        result = []
        letters_dict = {}
        digit_logs = []

        for i, log in enumerate(logs):
            split_log = (word for word in log.split())
            prefix = next(split_log)

            if 'let' in prefix:
                letters_dict[prefix] = " ".join(w for w in split_log)
            else:
                digit_logs.append(i)

        result += [k + ' ' + v for (k, v) in sorted(letters_dict.items(), key=lambda x: x[1] + x[0])]
        result += [logs[i] for i in digit_logs]
        return result
```

Solution 2 - failing for logs which have the same key (e.g. 8), e.g.:  
`["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]`  
Lessons learned:  
be careful when using dicts for sorting/reorganizing data - they can eat up values (unless you use `defaultdict(list)`)  

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) <= 1:
            return logs

        result = []
        letters_dict = {}
        digit_logs = []

        for i, log in enumerate(logs):
            split_log = (word for word in log.split())
            prefix = next(split_log)
            rest = " ".join(w for w in split_log)

            if rest[0].isnumeric():
                digit_logs.append(i)
            else:
                letters_dict[prefix] = rest

        result += [k + ' ' + v for (k, v) in sorted(letters_dict.items(), key=lambda x: x[1] + x[0])]
        result += [logs[i] for i in digit_logs]
        return result
```

Solution 3 - successful

```python
class Solution:
   def reorderLogFiles(self, logs: List[str]) -> List[str]:
       if len(logs) <= 1:
           return logs

       result = []
       letter_logs = []
       digit_logs = []

       for i, log in enumerate(logs):
           split_log = (word for word in log.split())
           prefix = next(split_log)
           rest = " ".join(w for w in split_log)

           if rest[0].isnumeric():
               digit_logs.append(i)
           else:
               letter_logs.append((prefix, rest))

       result += [k + ' ' + v for (k, v) in sorted(letter_logs, key=lambda x: x[1] + x[0])]
       result += [logs[i] for i in digit_logs]
       return result
```

**Leetcode solution**:  

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
```

Lessons learned:  
- the `sorted()` callable doesn't use a parameter named "key" for no reason. Data can be sorted by key, and the key can be dynamically created from data with the use of a function.  
- any function can be passed to `sorted()` as something that generates keys from data: https://wiki.python.org/moin/HowTo/Sorting  
- an additional key like `0, 1...` etc. can be passed to the sort funtion to create **new, additional sorting hierarchy**  

I'm curious to understand how sorted is implemented under the hood, i.e. how's it heapify
or otherwise keep track of how data should be sorted.
