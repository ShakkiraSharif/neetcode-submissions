class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,value in enumerate(nums):
            need=target-value
            if need in dict:
                return [dict[need],index]
            dict[value]=index