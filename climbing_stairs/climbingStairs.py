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

# Runtime: 40 ms, faster than 13.53% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 53.21% of Python3 online submissions for Climbing Stairs.
