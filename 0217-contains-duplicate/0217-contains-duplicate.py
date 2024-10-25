class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set() #empty set

        for num in nums: #for loop through nums
            if num in seen: #add number to the set, sets only have unique values
                return True
            else:
                seen.add(num) #else, add it to the set
        return False #if it goes through all the nums WITHOUT returning True for a dupe, return False


        