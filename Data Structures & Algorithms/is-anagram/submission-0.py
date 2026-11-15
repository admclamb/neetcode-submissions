class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = {}
        for char in s:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1

        for char in t:
            if char in occurrences:
                occurrences[char] -= 1
            else:
                occurrences[char] = -1
        
        return sum(abs(v) for v in occurrences.values()) == 0

        