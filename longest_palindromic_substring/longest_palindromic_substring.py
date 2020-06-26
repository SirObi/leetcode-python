class Solution:
   def longestPalindrome(self, s: str) -> str:

       # Sometimes it helps to deal with the small edge cases first
       # So that you can simplify your code for longer inputs
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
