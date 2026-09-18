class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        sorted_hm = sorted(hm.items(), key = lambda item: item[1], reverse = True)

        result = []

        for i in range(k):
            result.append(sorted_hm[i][0])
        
        return result