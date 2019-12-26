# passes with abcabcbb, bbbbb, pwwkew
# fails with dvdf

class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:
        longest = 0
        
        substring_chars = set()
        curr_length = 0
        for c in input_string:
            current_char = {c}
            substring_chars.update(current_char)
            
            new_length = len(substring_chars)
            if new_length > curr_length:
                curr_length = new_length
                longest = max(curr_length, longest)
            else:
                substring_chars = current_char
                curr_length = 0
        return longest
        
