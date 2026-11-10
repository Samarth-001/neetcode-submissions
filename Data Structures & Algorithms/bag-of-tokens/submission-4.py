class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        l = 0
        r = len(tokens) - 1
        score = 0
        ans = 0

        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                ans = max(ans, score)

            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1

            else:
                break

        return ans