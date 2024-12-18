class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if(len(s) < k):
            return 0


        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char,0) +1
        
        for char in char_count:
            if char_count[char] < k:
                substrings = s.split(char)
                return max(self.longestSubstring(sub, k) for sub in substrings)

        return len(s)