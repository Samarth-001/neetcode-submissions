# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l = 0

        while l<=n:
            mid = int(l+(n-l)/2)
            
            id = guess(mid)
            if id == 0:
                return mid
            elif id == -1:
                n = mid-1
            else:
                l = mid+1
            