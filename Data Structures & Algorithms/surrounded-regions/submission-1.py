class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()

        def find(i,j):
            visited.add((i,j))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for ni, nj in directions:
                ni += i
                nj += j

                if (ni>=0 and ni<len(board)) and (nj>=0 and nj<len(board[0])) and ((ni,nj) not in visited) and board[ni][nj] == "O":
                    find(ni,nj)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j] == "O":
                    find(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    board[i][j] = "X"
        # print(visited)

        