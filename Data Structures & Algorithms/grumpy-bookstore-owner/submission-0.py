class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        l,r=0,0

        gsum = 0
        ngsum = 0
        count = 0

        while r<len(customers):
            if grumpy[r] == 0:
                ngsum+=customers[r]
            else:
                count+=customers[r]

            if r-l>=minutes-1:
                gsum = max(gsum,count)
                if grumpy[l] == 1:
                    count = count-customers[l]
                l+=1
            r+=1
        
        return ngsum + gsum