class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position, speed = map(
            list,
            zip(*sorted(zip(position, speed), key=lambda x: x[0], reverse=True))
        )

        max_val = 0
        out = 0


        for i, val in enumerate(position):
            time_val = (target - position[i]) / speed[i]

            if time_val > max_val:
                out = out + 1
                max_val = time_val
        
        return out
        
