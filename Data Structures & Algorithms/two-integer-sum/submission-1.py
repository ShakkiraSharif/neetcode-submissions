class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta={}
        for i,n in enumerate(nums):
            num=target-n
            if num in dicta:
                return [dicta[num],i]
            dicta[n]=i

        