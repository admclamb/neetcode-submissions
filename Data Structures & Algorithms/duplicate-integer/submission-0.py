class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            if num in occurences:
                return True
            else:
                occurences[num] = 1
        
        return False

        