class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        for c in nums:
            if c not in seen:
                seen.append(c)
        print(seen)
        if seen==nums:
            return False
        return True