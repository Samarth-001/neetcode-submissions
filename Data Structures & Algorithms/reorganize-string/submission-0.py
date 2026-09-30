import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hm = {}
        
        hm = Counter(s) 

        # print(hm)

        heap = []
        for key, value in hm.items():
            heapq.heappush(heap, (-value, key))
        
        # print(heap)

        ans = ""
        while heap:
            val, ch = heapq.heappop(heap)
            if ans and ans[-1] == ch:
                if not heap:
                    return ""

                val1, ch1 = heapq.heappop(heap)
                
                if ch1 == ans[-1]:
                    return ""
                
                ans+=ch1
                
                if val1<-1:
                    val1+=1
                    heapq.heappush(heap, (val1,ch1))
                
                heapq.heappush(heap, (val,ch))
                continue
            else:
                ans+=ch
            
            if val< -1:
                val+=1
                heapq.heappush(heap, (val,ch))


        # print(ans)
        return ans