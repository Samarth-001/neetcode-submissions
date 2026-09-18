class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm_r = {}
        hm_c = {}
        hm_b = {}

        for row in range(9):
            hm_r[row] = []
            hm_c[row] = []
            hm_b[row] = []

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)

                if val not in hm_r[i]:
                    hm_r[i].append(val)
                else:
                    return False

                if val not in hm_c[j]:
                    hm_c[j].append(val)
                else:
                    return False

                if val not in hm_b[box]:
                    hm_b[box].append(val)
                else:
                    return False

        return True