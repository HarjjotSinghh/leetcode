from typing import List


# My Solution
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        best_sum = [[0] * (n + 1) for _ in range(4)]
        best_index = [[0] * (n + 1) for _ in range(4)]
        for t in range(1, 4):
            for i in range(k * t, n + 1):
                current_sum = prefix_sum[i] - prefix_sum[i - k] + best_sum[t - 1][i - k]
                if current_sum > best_sum[t][i - 1]:
                    best_sum[t][i] = current_sum
                    best_index[t][i] = i - k
                else:
                    best_sum[t][i] = best_sum[t][i - 1]
                    best_index[t][i] = best_index[t][i - 1]
        result = [0] * 3
        end = n
        for t in range(3, 0, -1):
            result[t - 1] = best_index[t][end]
            end = result[t - 1]
        return result


# Best / Most Optimal Solution
class Solution2:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        best_single_start = 0
        best_double_start = [0, k]
        best_triple_start = [0, k, k * 2]
        current_window_sum_single = sum(nums[:k])
        current_window_sum_double = sum(nums[k : k * 2])
        current_window_sum_triple = sum(nums[k * 2 : k * 3])
        best_single_sum = current_window_sum_single
        best_double_sum = current_window_sum_single + current_window_sum_double
        best_triple_sum = (
            current_window_sum_single
            + current_window_sum_double
            + current_window_sum_triple
        )
        single_start_index = 1
        double_start_index = k + 1
        triple_start_index = k * 2 + 1
        while triple_start_index <= len(nums) - k:
            current_window_sum_single = (
                current_window_sum_single
                - nums[single_start_index - 1]
                + nums[single_start_index + k - 1]
            )
            current_window_sum_double = (
                current_window_sum_double
                - nums[double_start_index - 1]
                + nums[double_start_index + k - 1]
            )
            current_window_sum_triple = (
                current_window_sum_triple
                - nums[triple_start_index - 1]
                + nums[triple_start_index + k - 1]
            )
            if current_window_sum_single > best_single_sum:
                best_single_start = single_start_index
                best_single_sum = current_window_sum_single
            if current_window_sum_double + best_single_sum > best_double_sum:
                best_double_start[0] = best_single_start
                best_double_start[1] = double_start_index
                best_double_sum = current_window_sum_double + best_single_sum
            if current_window_sum_triple + best_double_sum > best_triple_sum:
                best_triple_start[0] = best_double_start[0]
                best_triple_start[1] = best_double_start[1]
                best_triple_start[2] = triple_start_index
                best_triple_sum = current_window_sum_triple + best_double_sum
            single_start_index += 1
            double_start_index += 1
            triple_start_index += 1
        return best_triple_start
