class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            c = s[i]
            d = s[len(s)-i-1]

            s[i] = d
            s[len(s)-i-1] = c