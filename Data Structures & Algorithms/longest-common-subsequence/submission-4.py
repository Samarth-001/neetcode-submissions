class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}

        def find(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in mem:
                return mem[(i, j)]

            if text1[i] == text2[j]:
                mem[(i, j)] = 1 + find(i + 1, j + 1)
            else:
                mem[(i, j)] = max(
                    find(i + 1, j),
                    find(i, j + 1)
                )

            return mem[(i, j)]

        return find(0, 0)