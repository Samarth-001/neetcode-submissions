class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inbound = [0]*n
        outbound = [0]*n

        for t in trust:
            inbound[t[1]-1]+=1
            outbound[t[0]-1]+=1

        print(inbound)
        print(outbound)
        
        for i in range(len(outbound)):
            print(i)
            if outbound[i] == 0 and inbound[i] == n-1:
                return i+1
        
        return -1