

# My Solution
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        n = len(words)
        last = words[n - 1][-1]
        for i in range(n):
            if words[i][0] != last:
                return False
            last = words[i][-1]
        return True
    
# Best / Most Optimal Solution
class Solution2:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        s = sentence.split()
        print(s,s[0],s[-1])
        if len(s) == 1:
            s=''.join(s)
            if s[0] == s[-1]:
                return True
            else:
                return False
        for i in range(len(s)-1):
            if s[i][-1] != s[i+1][0]:
                return False
        return True
