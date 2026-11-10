class Solution:
    def reverseWords(self, s: str) -> str:
        pass

        arr = s.split(" ")
        print(arr)

        ans = ""

        for i in range(len(arr)):
            
            word = arr[i]
            r = len(word)-1

            while r>-1:
                ans += word[r]
                r-=1
            
            if i<(len(arr)-1):
                ans += " "
        
        return ans