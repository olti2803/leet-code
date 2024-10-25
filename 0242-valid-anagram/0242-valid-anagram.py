class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # simple sort for both s and t, seperating each char in order
        sorted_s = sorted(s) 
        sorted_t = sorted(t)

        if (sorted_s == sorted_t): # if they're the same, its a valid anagram, return true
            return True
        else:
            return False # if not, return false

        
