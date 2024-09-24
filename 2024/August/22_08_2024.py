
# My Solution
class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num).split('b')
        m=n[1]
        s=''
        for i in m:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
    
# Best / Most Optimal Solution
class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)[2:]
        v=str(s)
        l=[]
        for i in v:
            if i=="0":
                l.append("1")
            else:
                l.append("0")
        v=''.join(l)
        b=int(v,2)
        return b
