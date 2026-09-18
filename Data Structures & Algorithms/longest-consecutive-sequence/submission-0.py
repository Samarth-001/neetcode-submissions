class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if i not in hm:
                hm[i] = 1
        res = 0
        for i in nums:
            if i-1 not in hm:
                curr_len = 1
                val = i
                while(True):
                    if val+1 in hm:
                        curr_len += 1
                        val += 1
                    else:
                        break
                res = max(res, curr_len)

        return res
