## Summary  
I've had the correct instinct to use a dictionary to keep track of the state of the items added.  
My mistake was in trying to use a heap for accessing the latest item easily.  
Inevitably, I would run into the problem of having to search the heap and delete an "updated" task.  
Although I guess, in the wild, this problem _has_ been solved.  

In any case, the OrderedDict provides the O(1) put and get functionality - from `dict`. 
It also provides the linked list functionality of being able to delete the first/last item (if you pass it to an iterator).  

Additional:  
put can be either add or update task.

## Code  

Solution 1.  
Lessons learned:  
- a cache needs to have the ability to **update** an entry.  

```python
from datetime import datetime


class LRUCache():

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.queue = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.put(key, self.cache[key])
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.maxsize:
            _, k = self.queue.pop()
            del self.cache[k]
        heappush(self.queue, (datetime.now(), key))
        self.cache[key] = value
```

Testcase:  
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

Fails:  
["LRUCache","put","put", "put", "get"]
[[2],[1,1],[2,2],[1,7],[1]]


Solution 2.  

Lessons learned:  
- using arrays as quees can get complicated when you need to update a task (even if you heapify)  

```python
from datetime import datetime


class LRUCache():

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.queue = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.put(key, self.cache[key])
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.maxsize:
            _, k = heappop(self.queue)
            del self.cache[k]
        heappush(self.queue, (datetime.now(), key))
        self.cache[key] = value
```

Fails:
["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]


Solution 3.  

Lessons learned:  
- same as above  

```python
class LRUCache():

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.queue = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.put(key, self.cache[key])
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.maxsize:
            if key in self.cache:
                self.cache[key] = value
            else:
                _, k = heappop(self.queue)
                del self.cache[k]
        heappush(self.queue, (datetime.now(), key))
        self.cache[key] = value
```

Fails:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]


Solution 4. (based on Leetcode solution)  

Lessons learned:  
- OrderedDict keeps track of items' state AND the order in which they were added  

```python
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.maxsize = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def put(self, key: int, value: int) -> None:
        if len(self) == self.maxsize:
            if key in self:
                del self[key]
                self[key] = value
                self.move_to_end(key)
            else:
                lru_item = next(iter(self))
                del self[lru_item]
        self[key] = value
```

Fails:  
5 other test cases, out of 18.  
The one that fails first is a gigantic one, so hard to say what went wrong.  


This passes (I forgot to specify the newly added key should be treated as the "freshest"):  

```python
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.maxsize = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def put(self, key: int, value: int) -> None:
        if len(self) == self.maxsize:
            if key in self:
                del self[key]
                self[key] = value
                self.move_to_end(key)
            else:
                lru_item = next(iter(self))
                del self[lru_item]
        self[key] = value
        self.move_to_end(key)
```
        
Slightly cleaned up:  

```python
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.maxsize = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def put(self, key: int, value: int) -> None:
        if len(self) == self.maxsize:
            if key in self:
                del self[key]
            else:
                lru_item = next(iter(self))
                del self[lru_item]
        self[key] = value
        self.move_to_end(key)
```
