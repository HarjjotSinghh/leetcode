
# My Solution
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:        
        ans = numW = blocks[:k].count('W')
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                numW += 1
            if blocks[i-k] == 'W':
                numW -= 1
            ans = min(ans, numW)      
        return ans

# Best / Most Optimal Solution
class Solution2:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=0
        for i in range(k):
            if blocks[i]=='W':
                c+=1
        a,l=c,0
        for i in range(k,len(blocks)):
            if blocks[l]=='W':
                c-=1
            l+=1
            if blocks[i]=='W':
                c+=1
            a=min(a,c)
        return a
