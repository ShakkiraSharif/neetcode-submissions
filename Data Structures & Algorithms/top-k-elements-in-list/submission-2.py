class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        op = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        top = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        top = top[:k]

        for key, value in top:
            op.append(key)

        return op