from collections import defaultdict

# My Solution
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        i = 0
        letter_to_dict = [defaultdict(int) for _ in range(26)]
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            for k in range(1, j - i + 1):
                letter_to_dict[ord(s[i]) - ord('a')][k] += j - i - k + 1
            i = j
        result = 0
        for letter_dict in letter_to_dict:
            result = max(result, max((k for k, v in letter_dict.items() if v>=3), default=0))
        return -1 if result == 0 else result

# Best / Most Optimal Solution
class Solution2:
    def maximumLength(self, s: str) -> int:
        cnt_dict = defaultdict(list)
        cnt = 0
        current_c = None
        s = s + "1"
        for c in s:
            if not current_c:
                current_c = c
            if current_c == c:
                cnt += 1
            else:
                cnt_dict[current_c].append(cnt)
                current_c = c
                cnt = 1
        ans = -1
        for k, v in cnt_dict.items():
            v = sorted(v, reverse=True)
            if v[0] > 2:
                ans = max(v[0]-2, ans)
            if len(v) >= 2 and v[0] > 1:
                ans = max(min(v[0]-1, v[1]), ans)
            if len(v) >= 3:
                ans = max(ans, v[2])
        return ans
