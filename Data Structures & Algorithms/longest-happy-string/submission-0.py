class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        if a==b and b==c and c==0:
            return ""
        

        heap = []
        if a>0:
            heapq.heappush(heap, (-a, 'a'))
        if b>0:
            heapq.heappush(heap, (-b, 'b'))
        if c>0:
            heapq.heappush(heap, (-c, 'c'))

        
        ans = ""
        while heap:
            val, ch = heapq.heappop(heap)
            if len(ans)>1 and ans[-1] == ch and ans[-2] == ch:
                if not heap:
                    return ans

                val1, ch1 = heapq.heappop(heap)
                ans += ch1

                if val1<-1:
                    val1+=1
                    heapq.heappush(heap,(val1,ch1))
                
                heapq.heappush(heap,(val,ch))
                continue
            else:
                ans+=ch
            
            if val<-1:
                val+=1
                heapq.heappush(heap,(val,ch))
        
        return ans