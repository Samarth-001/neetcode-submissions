class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        balls = 0
        pre = 0  
        
        left = []
        
        for i in range(len(boxes)):
            left.append(balls + pre)
            pre = left[i]

            if boxes[i] == "1":
                balls +=1
        
        # print(left)

        balls = 0
        pre = 0
        
        right = []
        
        for i in range(len(boxes)-1,-1,-1):
            right.append(balls + pre)
            pre = right[-1]

            if boxes[i] == "1":
                balls +=1
        
        # print(right)
        ans = []
        
        for i in range(len(boxes)):
            ans.append(right[len(boxes)-i-1] + left[i])

        # print(ans)
        return ans