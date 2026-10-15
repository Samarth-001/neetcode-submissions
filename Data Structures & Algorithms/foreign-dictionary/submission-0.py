class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
                indegree[char] = 0

        # Build ordering constraints
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            # Invalid prefix case
            if len(first) > len(second) and first.startswith(second):
                return ""

            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
        
        # print(graph)
        # print(indegree)

        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
        
        # print(queue)
        ans = ""

        while queue:
            # print(indegree)
            for _ in range(len(queue)):
                char = queue.popleft()
                ans += char
                indegree.pop(char)
                
                for neighbor in graph[char]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                

        if len(indegree)>0:
            return ""
        return ans




