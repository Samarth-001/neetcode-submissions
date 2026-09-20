class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l = 0
        r = mountainArr.length()-1
        ans = 0

        while l<=r:
            mid = int(l + ((r-l)/2))

            if mountainArr.get(mid)>mountainArr.get(mid-1) and mountainArr.get(mid)> mountainArr.get(mid+1):
                ans = mid
                break
            elif mountainArr.get(mid)>mountainArr.get(mid-1) and mountainArr.get(mid)<mountainArr.get(mid+1):
                l=mid+1
            else:
                r=mid-1

        l = 0
        r = ans

        # print(l,r)
        while l<=r:
            mid = int(l + ((r-l)/2))
            midVal = mountainArr.get(mid)
            # print(mid)

            if midVal==target:
                return mid
            elif midVal<target:
                l = mid+1
            else:
                r = mid-1
        
        l = ans+1
        r = mountainArr.length()-1

        # print(l,r)
        while l<=r:
            mid = int(l + ((r-l)/2))
            midVal = mountainArr.get(mid)
            # print(mid)

            if midVal==target:
                return mid
            elif midVal>target:
                l = mid+1
            else:
                r = mid-1

        return -1               