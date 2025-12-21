class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            # If s[r] is in map and is inside the current window, we must jump l
            if s[r] in char_map and char_map[s[r]] >= l:
                l = char_map[s[r]] + 1
            
            # Always update the character's latest index
            char_map[s[r]] = r
            
            # Always update max_length
            max_length = max(max_length, r - l + 1)
            
        return max_length
