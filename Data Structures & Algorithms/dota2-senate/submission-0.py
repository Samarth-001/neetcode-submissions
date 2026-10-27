class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)
        rQueue = deque()
        dQueue = deque()

        for i in range(len(senate)):
            if senate[i]=='R':
                rQueue.append(i)
            if senate[i]=='D':
                dQueue.append(i)

        # print(rQueue)
        # print(dQueue)
        
        while len(rQueue)>0 and len(dQueue)>0:
            rval = rQueue.popleft()
            dval = dQueue.popleft()

            if rval<dval:
                rQueue.append(rval+n)
            else:
                dQueue.append(dval+n)
        
        if len(rQueue)>0:
            return 'Radiant'
        return 'Dire'