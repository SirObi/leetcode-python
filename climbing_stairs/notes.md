## Summary  
As most recursive problems in Python, this can be solved via recursion or iteration.  
My recursive solution was quite slow (compared to other people).  
So I've tested out an iterative approach, as well.  
As I expected, the iterative solution was faster, if more awkward looking.  

This exercise is made much easier if you notice that 1, 2, 3, (5) etc. make a Fibonacci  
sequence. But it's easy to miss, especially if you don't write a test case for 4 (output: 5).  


## Initial Notes
brute force solution would be to check all possible combinations of 1s and 2s that give n  
big O of that is 2^n.  
The complexity we want to get down to is O(n).  
We want access to the result of previously done computations, so we'll use a dict to cache them.  

## Code  

Solution 1. (recursive)  

```python
class Solution:
    cache = {
            1: 1,
            2: 2
        }

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        res1 = self.climbStairs(n-1)
        res2 = self.climbStairs(n-2)
        self.cache[n] = res1 + res2
        return res1 + res2
```

Solution 2. (iterative)  

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        cache  = []
        cache.append(0)
        cache.append(1)
        cache.append(2)

        for i in range(3, n+1):
            cache.append(cache[i - 1] + cache[i - 2])
        return cache[n]
```
Runtime: 28 ms, faster than 74.17% of Python3 online submissions for Climbing Stairs.  
Memory Usage: 13.8 MB, less than 44.57% of Python3 online submissions for Climbing Stairs.  
