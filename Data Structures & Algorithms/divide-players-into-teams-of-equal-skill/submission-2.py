class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pass

        pairs = len(skill)/2
        target = sum(skill)/pairs
        
        ans = 0
        
        hm = {}

        for skil in skill:
            if target - skil not in hm:
                hm[skil] = hm.get(skil,0)+1
            else:
                ans += (skil * (target-skil))
                if hm[target-skil] == 1:
                    v = hm.pop((target-skil), None)
                else:
                    hm[target-skil] -=1
        
        if len(hm)>0:
            return -1
        
        return int(ans)