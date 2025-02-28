# My Solution
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)
        prev_row = [str2[0:col] for col in range(str2_length + 1)]
        for row in range(1, str1_length + 1):
            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    pick_s1 = prev_row[col]
                    pick_s2 = curr_row[col - 1]
                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )
            prev_row = curr_row
        return prev_row[str2_length]


# Best / Most Optimal Solution
class Solution2:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        shorter, longer = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        shorter, longer, initial_common_subsequence = self.find_initial_common_subsequence(shorter, longer)
        remaining_common_subsequence = self.find_longest_common_subsequence(shorter, longer)
        return initial_common_subsequence + remaining_common_subsequence
    def find_initial_common_subsequence(self, shorter: str, longer: str) -> (str, str, str):
        initial_common_subsequence = ''
        shorter_index = 0
        longer_index = 0
        shorter_last_index = len(shorter) - 1
        longer_last_index = len(longer) - 1
        while shorter_index < shorter_last_index and longer_index < longer_last_index:
            if shorter[shorter_index] == longer[longer_index]:
                initial_common_subsequence += shorter[shorter_index]
            else:
                break
            shorter_index += 1
            longer_index += 1
        return shorter[shorter_index:], longer[longer_index:], initial_common_subsequence
    def find_longest_common_subsequence(self, shorter: str, longer: str) -> str:
        if not shorter or not longer:
            return ''
        mp = MatrixProcessor()
        mp.build_subsequence_matrix(shorter, longer)
        return mp.find_supersequence()
class MatrixProcessor:
    def find_supersequence(self) -> str:
        supersequence = ''
        shorter_index, longer_index = 0, 0
        while shorter_index < self.shorter_len and longer_index < self.longer_len:
            shorter_symbol = self.shorter[shorter_index]
            longer_symbol = self.longer[longer_index]
            if shorter_symbol == longer_symbol:
                supersequence += shorter_symbol
                shorter_index += 1
                longer_index += 1
            else:
                use_shorter = self.matrix[longer_index][shorter_index + 1] > self.matrix[longer_index + 1][shorter_index]
                if use_shorter:
                    supersequence += shorter_symbol
                    shorter_index += 1
                else:
                    supersequence += longer_symbol
                    longer_index += 1
        while shorter_index < self.shorter_len:
            supersequence += self.shorter[shorter_index]
            shorter_index += 1
        while longer_index < self.longer_len:
            supersequence += self.longer[longer_index]
            longer_index += 1
        return supersequence
    def build_subsequence_matrix(self, shorter: str, longer: str) -> None:
        self.shorter, self.longer = shorter, longer
        self.shorter_len, self.longer_len = len(self.shorter), len(self.longer)
        self.longer_index = self.longer_len - 1
        previous_row = self._build_shorter_empty_row()
        matrix = [previous_row]
        while self.longer_index >= 0:
            previous_row = self._build_next_row_from_bottom(previous_row)
            matrix.append(previous_row)
            self.longer_index -= 1
        self.matrix = matrix[::-1]
    def _build_shorter_empty_row(self) -> list[int]:
        return [0] * (self.shorter_len + 1)
    def _build_next_row_from_bottom(self,  previous_row: list[int]) -> (list[int], int, int):
        next_row = self._build_shorter_empty_row()
        longer_symbol = self.longer[self.longer_index]
        for shorter_index in range(self.shorter_len - 1, -1, -1):
            shorter_symbol = self.shorter[shorter_index]
            if shorter_symbol == longer_symbol:
                shorter_index_value = previous_row[shorter_index + 1] + 1
            else:
                shorter_index_value = max(next_row[shorter_index + 1], previous_row[shorter_index])
            next_row[shorter_index] = shorter_index_value
        return next_row
