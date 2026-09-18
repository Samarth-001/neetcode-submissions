class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)

        boats = len(people)
        l=0
        r=boats-1

        while(l<r):
            if people[l]+people[r]<=limit:
                boats-=1
                l+=1
                r-=1
            else:
                r-=1

        return boats

        # [1,2,4,5]
        # [1,2,2,3,3]

        [1,2,6,7]