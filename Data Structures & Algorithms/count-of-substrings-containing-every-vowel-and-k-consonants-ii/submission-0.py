class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        hm = {
            'a': -1,
            'e': -1,
            'i': -1,
            'o': -1,
            'u': -1
        }

        consonants = [-1]
        ans = 0

        for i in range(len(word)):
            ch = word[i]

            if ch in hm:
                hm[ch] = i
            else:
                consonants.append(i)

            vowel_min = min(
                hm['a'],
                hm['e'],
                hm['i'],
                hm['o'],
                hm['u']
            )

            if vowel_min == -1:
                continue

            if k == 0:
                left_min = consonants[-1] + 1
                left_max = vowel_min

            else:
                if len(consonants) < k + 1:
                    continue

                left_min = consonants[-k-1] + 1
                left_max = min(vowel_min, consonants[-k])

            if left_min <= left_max:
                ans += left_max - left_min + 1

        return ans