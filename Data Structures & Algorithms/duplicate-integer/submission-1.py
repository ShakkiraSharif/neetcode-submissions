class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        if any(value>1 for value in count.values()):
            return True
        else:
            return False
         
                       