
# My Solution
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring

# Best / Most Optimal Solution
class Solution2:
    def findTheLongestSubstring(self, s: str) -> int:
        n=len(s)
        ss={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for c in s:
            if c in 'aeiou':
                ss[c]+=1
        for i in range(len(s),0,-1):
            if n-i>0 and s[i] in 'aeiou':
                ss[s[i]]-=1
            sss = ss.copy()
            if all((value % 2 == 0 or value ==0) for value in ss.values()):
                return i
            for j in range(1,len(s)-i+1):
                if s[j-1] in 'aeiou':
                    sss[s[j-1]]-=1
                if s[j+i-1] in 'aeiou':
                    sss[s[j+i-1]]+=1
                if all((value % 2 == 0 or value ==0) for value in sss.values()):
                    return i
        return 0
