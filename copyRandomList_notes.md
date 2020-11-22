This doesn’t work, because second Node.random doesn’t point to head, for input:  
`[[7,null],[13,0],[11,4],[10,2],[1,0]]`
 

```

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from copy import deepcopy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        output = deepcopy(head)
        head_pointer = output
        
         while output is not None:
             output.next = deepcopy(output.next)
             output = output.next
            
        return output
```


This works and passes submission:

```

from copy import deepcopy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return deepcopy(head)
        
```


Looking at alternative solutions, my very initial intuition to use a hash to track visited nodes was correct

This is how you deecopy an object without using the deepcopy library:

`node = Node(head.val, None, None)`


Deepcopying is instantiating a new object with all the values the same as the copied object.
(Simply using the assignment operator won’t work).
