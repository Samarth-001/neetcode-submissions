class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check(k):
            removed = [False] * len(s)

            for i in range(k):
                removed[removable[i]] = True

            j = 0

            for i in range(len(s)):
                if removed[i]:
                    continue

                if s[i] == p[j]:
                    j += 1

                    if j == len(p):
                        return True

            return False

        l, r = 0, len(removable)

        while l <= r:
            mid = l + (r - l) // 2

            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r