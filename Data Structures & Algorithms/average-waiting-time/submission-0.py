class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        time = 0
        ans = 0.00
        
        for cust in customers:
            arrival = cust[0]
            wtime = cust[1]

            if arrival>time:
                time = arrival
            
            time += wtime

            print(time, arrival)
            ans += (time-arrival)
        
        return ans/len(customers)