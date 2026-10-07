class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        visited = set()
        queue = deque()
        queue.append("0000")

        for i in deadends:
            visited.add(i)

        def generateStates(point):

            for i in range(len(point)):
                dig = int(point[i])
                up = (dig + 1) % 10
                down = (dig - 1) % 10

                sup = point[:i] + str(up) + point[i+1:]
                sdo = point[:i] + str(down) + point[i+1:]

                if sup not in visited:
                    queue.append(sup)
                    visited.add(sup)
                if sdo not in visited:
                    queue.append(sdo)
                    visited.add(sdo)

        ans = -1

        while queue:
            ans+=1
            for _ in range(len(queue)):
                el = queue.popleft()
                if el==target:
                    return ans
                generateStates(el)

        
        return -1
