class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        mid = 0
        while l<=r:
            mid = int(l+((r-l)/2))

            # print(l, mid, r)

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid -1
            else:
                l = mid + 1

        # print(target,matrix[mid][0])
        if matrix[mid][0] < target:
            row = mid
        else:
            row = mid-1

        l = 0
        r = len(matrix[0])-1

        while l<=r:
            mid = int(l+((r-l)/2))

            print(l, mid, r)

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                l = mid + 1

        
        return False