class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 0:
            return []

        m = -1
        for i in range(len(arr)-1,-1,-1):
            # print(arr[i])
            t = arr[i]
            arr[i] = m
            m = max(t, m)
        
        return arr