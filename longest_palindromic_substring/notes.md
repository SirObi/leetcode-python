## Summary  
For this intuition, I had the right instinct from the start:
- I knew I had to use some sort of dynamic programming  
- I knew there were two possible types of palindromes: one with the centre of the palindrome being a letter, and one with the centre being between two letters.  
- I knew growing the palindrome based on those shorter palindromes was the way to go.  

I lost 90% of my time due to issues such as:  
- off-by-one errors (array)  
- tracking state in my head (while loop)  

## Code  
Solution 3 or 4:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return False
        
        if len(s) == 1:
            return 1
    
        longest_start = 0
        longest_stop = 0
    
        for i in range(len(s)):
            start = i
            stop = i + 1
        
            while start >= 0 and stop < len(s):
                print(f"start {start} stop {stop}")
                if s[stop] != s[stop]:
                    break
                    
                if stop - start > longest_stop - longest_start:
                    longest_start = start
                    longest_stop = stop
                    print(f"longest start {longest_start} longest stop {longest_stop}")
                start -=1
                stop += 1
            
            start = i
            stop = i + 1
            while start >= 0 and stop + 1 < len(s):
                if s[stop] != s[stop + 1]:
                    break
                if stop + 1 - start > longest_stop - longest_start:
                    longest_start = start
                    longest_stop = stop + 1
                start -= 1 
                stop += 1

    return s[longest_start:longest_stop]
```

# Solution 1/2        
#        ...
#        window_step = 1
#        longest_so_far = 1
#        longest_start, longest_stop = (0, 1)
#
#        for i in range(len(s)):
#            increase_stop = True
#            start = i
#            stop = i + window_step
#            window_size = stop - start
#            increase_stop = True
#            
#            if start > stop or len(s) - i < longest_so_far:
#                return s[longest_start:longest_stop]
#            
#            while start >= 0 and stop <= len(s) - 1:
#                print(f"start {start} stop {stop}")
#                print(s[start:stop])
#                if s[start] != s[stop -1] and s[start] != s[stop]:
#                    break
#                window_size += 1
#                if longest_so_far < window_size:
#                    longest_so_far = window_size
#                    longest_start = start
#                    longest_stop = stop
#                    
#                    if increase_stop:
#                        stop += 1
#                        increase_stop = False
#                    else:
#                        start -= 1
#                    
#        return s[longest_start:longest_stop]
        

Solution 4 or 5  
Lessons learned:  
it really pays to keep your functions short.  
Long, nested loops in one method is a recipe for cognitive overload.  
Factor out code into separate functions.  

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return None
        
        longest = 0
        longest_idxs = (0, 0)
        
        for i, _ in enumerate(s):
            length1, idxs1 = self.grow_window(s, i, i + 1)
            length2, idxs2 = self.grow_window(s, i, i + 2)
            if length1 > longest:
                longest = length1
                longest_idxs = idxs1
            if length2 > longest:
                longest = length2
                longest_idxs = idxs2
                    
        return s[longest_idxs[0]:longest_idxs[1] + 1]
        
    def grow_window(self, s: str, left: int, right: int) -> None:
        while left - 1 > 0 and right + 1 < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left) + 1, (left, right)
        
        
        
Testcases:
"babad"
"aaaab"
"cbbd"
```

Solution 6.  
Lessons learned:  
if you have a choice between one index and a tuple of indexes,  
using one index may save you some headache.  

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return None
        
        longest = 0
        start, stop = (0, 0)
        
        for i, _ in enumerate(s):
            length1 = self.grow_window(s, i, i + 1)
            length2 = self.grow_window(s, i, i + 2)
            if length1 > longest:
                longest = length1
                start = (i - length1 // 2) 
                stop = (i + length1 // 2)  
            if length2 > longest:
                longest = length2
                start = (i + 1 - length2 // 2)
                stop = (i + 2 + length2 // 2)
                    
        return s[start:stop]
        
    def grow_window(self, s: str, left: int, right: int) -> None:
        while left - 1 > 0 and right + 1 < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left) + 1
```

Solution 7. (fails with input 'ab')  
Lesson learned:  
if you have a function that includes a loop and returns something,  
make sure to have a default return value defined at the start of the function.  
It takes care of some less obvious, ugly use cases.  

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        
        longest = 0
        start, stop = (0, 0)
        
        for i, _ in enumerate(s):
            length1 = self.grow_window(s, i, i + 1)
            length2 = self.grow_window(s, i, i + 2)
            if length1 > longest:
                longest = length1
                start = (i - length1 // 2) + 1
                stop = (i + length1 // 2)  + 1
            if length2 > longest:
                longest = length2
                start = (i + 1 - length2 // 2)
                stop = (i + 2 + length2 // 2)
                    
        return s[start:stop]
        
    def grow_window(self, s: str, left: int, right: int) -> None:
        final_right, final_left = 0, 0
        while left >= 0 and right + 1 <= len(s) and s[left] == s[right]:
            final_right, final_left = right, left
            left -= 1
            right += 1
        return (final_right - final_left) + 1
```

        
First successful solution.
Lesson: once you get rid of the len=0 edge case, initialize "return" variables (like length) to  1

```python
class Solution:
   def longestPalindrome(self, s: str) -> str:
       if len(s) < 1:
           return ""

       longest = 1
       start, stop = (0, 1)

       for i, _ in enumerate(s):

length1 = self.grow_window(s, i, i + 1)
           length2 = self.grow_window(s, i, i + 2)
           if length1 > longest:
               longest = length1
               start = (i - length1 // 2) + 1
               stop = (i + length1 // 2)  + 1
           if length2 > longest:
               longest = length2
               start = (i + 1 - length2 // 2)
               stop = (i + 2 + length2 // 2)

       return s[start:stop]

   def grow_window(self, s: str, left: int, right: int) -> None:
       final_right, final_left = 0, 0
       while left >= 0 and right + 1 <= len(s) and s[left] == s[right]:
           final_right, final_left = right, left
           left -= 1
           right += 1
       return (final_right - final_left) + 1
```

Final, successful solution  
Lesson learned:  
Sometimes it helps to deal with the small edge cases first,
so that you can simplify the "meat" of your code that handles longer inputs.


```python
class Solution:
   def longestPalindrome(self, s: str) -> str:

       if len(s) < 2:
           return s

       if len(s) == 2 and s[0] == s[1]:
           return s 

       if len(s) == 3 and s[0] == s[2]:
           return s

       longest = 1
       start, stop = (0, 1)

       for i, _ in enumerate(s):
           length1 = self.grow_window(s, i, i + 1)
           length2 = self.grow_window(s, i, i + 2)
           if length1 > longest:
               longest = length1
               start = (i - length1 // 2) + 1
               stop = (i + length1 // 2)  + 1
           if length2 > longest:
               longest = length2
               start = (i + 1 - length2 // 2)
               stop = (i + 2 + length2 // 2)

       return s[start:stop]

   # You can also consider breaking down this function into 2  - 
   # one for 2 letters, one for 3
   def grow_window(self, s: str, left: int, right: int) -> None:
       final_right, final_left = 0, 0
       while left >= 0 and right + 1 <= len(s) and s[left] == s[right]:
           final_right, final_left = right, left
           left -= 1
           right += 1
       return (final_right - final_left) + 1
```
