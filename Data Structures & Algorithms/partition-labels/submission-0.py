class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hm={}
        for i in range(len(s)):
            hm[s[i]] = i

        maximumIndex = 0
        size = 0
        output = []
        for i in range(len(s)):
            size+=1

            if hm[s[i]] > maximumIndex:
                maximumIndex = hm[s[i]]
            
            if i == maximumIndex:
                output.append(size)
                size = 0

        return output