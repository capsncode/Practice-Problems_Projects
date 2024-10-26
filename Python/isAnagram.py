# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.


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