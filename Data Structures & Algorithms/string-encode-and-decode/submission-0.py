class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""

        for word in strs:
            enc_str += str(len(word))
            enc_str += "#"
            enc_str += word

        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_strs = []

        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]

            dec_strs.append(word)

            i = j + 1 + length

        return dec_strs