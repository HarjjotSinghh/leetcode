import math
from collections import Counter


# My Solution
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        sorted_tiles = "".join(sorted(tiles))
        return self._generate_sequences(sorted_tiles, "", 0, seen) - 1

    def _factorial(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 1
        for num in range(2, n + 1):
            result *= num
        return result

    def _count_permutations(self, seq: str) -> int:
        total = self._factorial(len(seq))
        for count in Counter(seq).values():
            total //= self._factorial(count)
        return total

    def _generate_sequences(self, tiles: str, current: str, pos: int, seen: set) -> int:
        if pos >= len(tiles):
            if current not in seen:
                seen.add(current)
                return self._count_permutations(current)
            return 0
        return self._generate_sequences(
            tiles, current, pos + 1, seen
        ) + self._generate_sequences(tiles, current + tiles[pos], pos + 1, seen)


# Best / Most Optimal Solution
class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_counter = Counter(tiles)
        result_counter = Counter([0])
        for tc in tile_counter.values():
            for l, n in list(result_counter.items()):
                for i in range(1, tc + 1):
                    result_counter[i + l] += math.comb(i + l, i) * n
        return sum(result_counter.values()) - 1
