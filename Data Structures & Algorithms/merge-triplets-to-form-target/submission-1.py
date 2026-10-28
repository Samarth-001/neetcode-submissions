class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        m1,m2,m3 = -1,-1,-1
        t1,t2,t3 = target
        for triplet in triplets:
            c1,c2,c3 = triplet
            if c1 <= t1 and c2 <= t2 and c3 <= t3:
                m1,m2,m3 = max(m1,c1),max(m2,c2),max(m3,c3)
        return (m1,m2,m3) == (t1,t2,t3)

        