class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False
        
        # Create dictionaries to store character counts
        s_count = {}
        t_count = {}
        
        # Count occurrences of each character in both strings
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Compare the character counts
        return s_count == t_count