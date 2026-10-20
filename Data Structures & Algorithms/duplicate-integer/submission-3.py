class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # create a hashmap
        for num in nums:
            if num in seen:
                return True # dupe found
            else:
                seen.add(num)
        return False # no dupes found
