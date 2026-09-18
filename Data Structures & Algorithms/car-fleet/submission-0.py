class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # position = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]

        # Sort by position descending
        position, speed = map(
            list,
            zip(*sorted(zip(position, speed), key=lambda x: x[0], reverse=True))
        )

        print(position)  # [7, 4, 1, 0]
        print(speed)     # [1, 2, 2, 1]

        stack = []

        for i, val in enumerate(position):
            time_val = (target - position[i]) / speed[i]

            if len(stack)<1:
                stack.append(time_val)
                continue


            if time_val > stack[-1]:
                stack.append(time_val)
        
        return len(stack)
        



        # 10
        # [7,4,1,0]
        # [1,8,2,1]
        # [3,0.8,5,9]
        