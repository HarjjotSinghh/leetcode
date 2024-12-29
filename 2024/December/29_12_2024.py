import collections
from typing import List


# My Solution
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        word_length = len(words[0])
        target_length = len(target)
        char_frequency = [[0] * 26 for _ in range(word_length)]
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1
        prev_count = [0] * (target_length + 1)
        curr_count = [0] * (target_length + 1)
        prev_count[0] = 1
        for curr_word in range(1, word_length + 1):
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                cur_pos = ord(target[curr_target - 1]) - ord("a")
                curr_count[curr_target] += (
                    char_frequency[curr_word - 1][cur_pos] * prev_count[curr_target - 1]
                ) % MOD
                curr_count[curr_target] %= MOD
            prev_count = curr_count.copy()
        return curr_count[target_length]


# Best / Most Optimal Solution
class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(target)
        num_word = len(words)
        n = len(words[0])
        MOD = 10**9 + 7
        pos_cnt = []
        for j in range(n):
            char2cnt = collections.defaultdict(int)
            for i in range(num_word):
                char2cnt[words[i][j]] += 1
            pos_cnt.append(char2cnt)
        dp = [[0] * n for _ in range(2)]
        for j in range(n - m + 1):
            if j == 0:
                dp[0][0] = pos_cnt[0][target[0]] % MOD
            else:
                dp[0][j] = (dp[0][j - 1] + pos_cnt[j][target[0]]) % MOD
        for i in range(1, m):
            dp[i % 2] = [0] * n
            for j in range(i, n - m + i + 1):
                dp[i % 2][j] = (
                    dp[i % 2][j - 1] + dp[(i - 1) % 2][j - 1] * pos_cnt[j][target[i]]
                ) % MOD
        return dp[(m - 1) % 2][n - 1]
