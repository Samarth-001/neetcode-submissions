class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fiver = 0
        ten = 0
        
        for bill in bills:
            print(fiver, ten)

            if bill == 5:
                fiver+=1
            
            elif bill == 10:
                if fiver == 0:
                    return False
                fiver-=1
                ten+=1
            
            elif bill == 20:
                if ten >=1:
                    if fiver>0:
                        fiver-=1
                        ten-=1
                        continue
                    else:
                        return False
                else:
                    if fiver >=3:
                        fiver-=3
                        continue
                    else:
                        return False

        return True    