class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        l = m-1
        r = n-1

        k = m+n-1

        while(k>=0):
            print(l,r)
            print(nums1)
            print(nums2)
            if l>=0 and r>=0:
                if nums1[l]>=nums2[r]:
                    nums1[k], nums1[l] = nums1[l], nums1[k]
                    l-=1
                else:
                    nums1[k] = nums2[r]
                    r-=1
            elif r>=0:
                nums1[k] = nums2[r]
                r-=1
            else:
                nums1[k], nums1[l] = nums1[l], nums1[k]
                l-=1

            k-=1