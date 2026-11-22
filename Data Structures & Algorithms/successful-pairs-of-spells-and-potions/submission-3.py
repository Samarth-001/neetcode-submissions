class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        n = len(potions)
        output = []

        for spell in spells:
            l, r = 0, n

            while l < r:
                mid = l + (r-l)//2

                if spell * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1

            output.append(n-l)

        return output