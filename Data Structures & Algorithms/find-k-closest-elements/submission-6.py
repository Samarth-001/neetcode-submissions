class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        minindex = 0
        for i in range(len(arr)):
            if (abs(arr[i] - x) < abs(x - arr[minindex])):
                minindex = i
        # print(minindex)

        l = 0
        r= len(arr)-1

        while(r-l)>=k:
            if abs(arr[l] - x) < abs(arr[r] - x):
                r-=1
            elif abs(arr[r] - x) < abs(arr[l] - x):
                l+=1
            else:
                if arr[r]>arr[l]:
                    r-=1
                else:
                    l+=1
        
        # print(arr[l:r+1])
        return arr[l:r+1]