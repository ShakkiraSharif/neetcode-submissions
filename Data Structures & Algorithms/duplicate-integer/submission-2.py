class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hassh=set()
        for num in nums:
            if num in hassh:
                return True
            hassh.add(num)
        return False