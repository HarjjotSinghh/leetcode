import sys
import json
from typing import List

# My Solution
class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0
class Solution:
    def __init__(self):
        self.root = trie_node()
    def insert(self, word):
        node = self.root
        for c in word:
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]
    def count(self, s):
        node = self.root
        ans = 0
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans
    def sumPrefixScores(self, words):
        N = len(words)
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            scores[i] = self.count(words[i])
        return scores

# Best / Most Optimal Solution
class Solution2:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        word_count = len(words)
        sorted_indices = sorted(range(word_count), key=lambda i: words[i])
        common_prefix_lengths = self._calculate_common_prefix_lengths(words, sorted_indices)
        scores = self._calculate_scores(words, sorted_indices, common_prefix_lengths)
        return scores
    def _calculate_common_prefix_lengths(self, words, sorted_indices):
        common_prefix_lengths = [0] * len(words)
        for i in range(1, len(words)):
            prev_word = words[sorted_indices[i - 1]]
            curr_word = words[sorted_indices[i]]
            common_length = 0
            while (common_length < len(prev_word) and 
                   common_length < len(curr_word) and 
                   prev_word[common_length] == curr_word[common_length]):
                common_length += 1
            common_prefix_lengths[i] = common_length
        return common_prefix_lengths
    def _calculate_scores(self, words, sorted_indices, common_prefix_lengths):
        scores = [0] * len(words)
        for i, word_index in enumerate(sorted_indices):
            word_length = len(words[word_index])
            scores[word_index] += word_length
            j = i + 1
            common_length = word_length
            while j < len(words):
                common_length = min(common_length, common_prefix_lengths[j])
                if common_length == 0:
                    break
                scores[word_index] += common_length
                scores[sorted_indices[j]] += common_length
                j += 1
        return scores
def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines)
    results = []
    for i in range(num_test_cases):
        words = json.loads(lines[i])
        result = Solution().sumPrefixScores(words)
        results.append(json.dumps(result, separators=(',', ':')))
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    kdsmain()
    exit(0)
