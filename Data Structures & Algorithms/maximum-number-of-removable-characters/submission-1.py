class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check(k):
            removed = set()

            for j in range(k):
                removed.add(removable[j])

            u, d = 0, 0

            while u < len(s) and d < len(p):

                if u in removed:
                    u += 1
                    continue

                if s[u] == p[d]:
                    d += 1

                u += 1

            return d == len(p)

        l, r = 0, len(removable)
        output = 0

        while l <= r:

            mid = l + (r - l) // 2

            if check(mid):
                output = mid
                l = mid + 1
            else:
                r = mid - 1

        return output