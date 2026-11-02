class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hset = set()

        for email in emails:
            
            local, host = email.split('@')
            local1 = ""
            
            for i in range(len(local)):
                if local[i] == '.':
                    continue
                if local[i] == '+':
                    break
                local1+=local[i]
            
            hset.add(local1+'@'+host)
        
        return len(hset)