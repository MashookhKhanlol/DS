from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)  # Dictionary to store grouped anagrams
        
        for string in strs:
            # Use sorted string as the key
            sorted_key = "".join(sorted(string))
            anagrams[sorted_key].append(string)
        
        # Return the grouped anagrams
        return list(anagrams.values())