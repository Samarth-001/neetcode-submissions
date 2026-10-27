class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize != 0:
            return False

        hand.sort()
        # print(hand)

        hm={}
        for val in hand:
            hm[val] = hm.get(val,0)+1

        # print(hm)

        for card in hand:
            if hm[card] == 0:
                continue
            
            for i in range(card, card+groupSize):
                if hm.get(i,-1) <=0:
                    return False
                hm[i]-=1
        
        return True