class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time=[]
        for i in range(len(position)):
            # print(position[i], speed[i])
            time.append((target - position[i]) / speed[i])
        
        # print(time)
        cars = list(zip(position,time))
        cars.sort(reverse = True)

        st = []
        fleet = 0
        for pos, time in cars:
            if st and st[-1]>=time:
                continue
            st.append(time)
            fleet+=1

        # print(fleet)
        return fleet