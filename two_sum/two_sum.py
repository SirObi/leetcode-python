class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for (i, v) in enumerate(nums):
            needed = target - v
            needed_idx = mapping.get(needed, None)
            if needed_idx is not None:
                return [i, needed_idx]
            mapping[v] = i
        return None

# Brute force: O(n^2), so we're probably looking for O(n) or O(log n)
# First solution:
# class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        candidates = [n for n in nums if n <= target]
#        for i1, c1 in enumerate(candidates):
#            for i2, c2 in enumerate(candidates):
#                if c1 + c2 == target and i1 != i2:
#                    return [i1, i2]

# Second solution:
#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        mapping = {v:i for (i, v) in enumerate(nums)}
#        for v, i in mapping.items():
#            needed = target - v
#            needed_has_idx = mapping.get(needed, False)
#            if needed_has_idx:
#                return [i, needed_has_idx]
#        return False

# Third solution
#from collections import defaultdict

#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        mapping = defaultdict(list)
#        for (i, v) in enumerate(nums):
#            mapping[v].append(i)
#        for v, idxs in mapping.items():
#            i = idxs.pop()
#            needed = target - v
#            needed_idxs = mapping.get(needed, False)
#            if needed_idxs:
#                return [i, needed_idxs[0]]
#        return None

