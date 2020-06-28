## Summary  
Some problems with arrays are best solved with 2 pointers - one on the left, one on the right.  
The computation ends when the index of the left pointer is greater or equal to the index of the right pointer.  


## Initial thought process  

# notes
# drawing a diagram is very helpful in this case

# Let's start simple
# 1. What happens if the array is all 0s?
# 2. What happens if the array has one element?
# 3. What happens if the array has two elements, but next to each other?
# 4. Can you simply apply the same technique for each height?
# 5. How would you calculate it for a simple case of [1, 0, 2]?
# 6. What's the brute force way of solving this? (O(n * k) - check each bar and each height.
# 7. What are the possible optimizations? - you should only check a given height, if there's more
# than one bar of this height.
# 8 Isn't this similar to counting islands?


## Code  

Solution 1.

Lessons learned:  
- if you end up with a solution where a value sits in several different categories, you might reconsider the solution  
- this is a clue for when to avoid dictionaries  
- creating a new iterator will start the count in that iterator from 0. - calling `next()` twice is how you iterate 2 items at a time.  

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        water = 0

        mapping = defaultdict(list)
        for i, elevation in enumerate(height):
            E = elevation
            while E > 0:
                mapping[E].append(i)
                E -= 1

        for level, v in mapping.items():
            if len(v) == 0:
                continue
            pairs = self.find_closest_neighbours(v)
            distances = sum((b - a for (a, b) in pairs))
            water += distances

        return water

    def find_closest_neighbours(self, bars: List[int]) -> int:
        first = (b for b in bars)
        second = (b for b in bars)

        pairs = zip(first, second)
        return pairs
```

Fails:  
[0,1,0,2,1,0,1,3,2,1,2,1]  

Solution 2.  

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        water = 0
        
        mapping = defaultdict(list)
        for i, elevation in enumerate(height):
            E = elevation
            while E > 0:
                mapping[E].append(i)
                E -= 1
        
        for level, v in mapping.items():
            if len(v) <= 1:
                continue
            pairs = self.find_closest_neighbours(v)
            distances = sum([b - a for (a, b) in pairs]) 
            water += (distances - 1) * level
            
        return water 
            
    def find_closest_neighbours(self, bars: List[int]) -> int:
        br = (b for b in bars)
        
        pairs = zip(br, br)
        return list(pairs)
```

Passes:  
[1, 0, 1]  

Fails:  
[2,0,2]  

Solution 3.  

Lessons learned:  
- one index is sometimes not enough for solving array-based problems  

```python  
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        water = 0
        
        is_open = False
        current_level = 0
        start = 0
        stop = 1
        
        for i, bar in enumerate(height):
            if is_open and bar > 0:
                stop = bar
                water += self.calculate_water(start, stop, current_level)
                start = stop
                current_level = bar
                
            if not is_open and bar > 0:
                is_open = True
                start = i
                current_level = bar
                
        return water
    
    def calculate_water(self, start, stop, current_level):
        return ((stop - start) - 1) * current_level
```

Passes:  
[2,0,2]  

Fails:  
[0,1,0,2,1,0,1,3,2,1,2,1]  

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        water = 0
        
        is_open = False
        current_level = 0
        obstacles = 0
        start = 0
        stop = 1
        
        for i, bar in enumerate(height):
            if is_open and bar > 0 and bar >= current_level:
                stop = i
                water += self.calculate_water(start, stop, current_level, obstacles)
                start = stop
                current_level = bar
                obstacles = 0
                
            elif not is_open and bar > 0:
                is_open = True
                start = i
                current_level = bar
            
            elif bar < current_level:
                obstacles += bar
                
        return water
    
    def calculate_water(self, start: int, stop: int, current_level: int, obstacles: int) -> int:
        print(f"{stop} - {start} = {((stop - start) - 1) * current_level}")
        return (((stop - start) - 1) * current_level) - obstacles
```

Still fails:  
[0,1,0,2,1,0,1,3,2,1,2,1] (misses the last one)  


Leetcode solution (in C++):  
use two pointers (left and right) nearing each other.  

Lessons learned:  
sometimes two pointers are necessary and make things much easier  


Final solution (faster than most)  

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        water = 0
        
        idx_left = 0
        idx_right = len(height) - 1
        left_max = 0
        right_max = 0
        
        while idx_left < idx_right:
            if height[idx_left] < height[idx_right]:
                if height[idx_left] >= left_max:
                    left_max = height[idx_left]
                else:
                    # there's space between left_max and right_max, so add it
                    water += left_max - height[idx_left]
                # move right
                idx_left += 1
                
            else:
                if height[idx_right] >= right_max:
                    right_max = height[idx_right]
                else:
                    # there's space between left_max and right_max, so add it
                    water += right_max - height[idx_right]
                # move left
                idx_right -= 1
        
        return water
```
