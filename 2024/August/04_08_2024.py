# My Solution
class Solution:
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7
        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                current_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum
        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            right = max_sum
            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, total_sum = count_and_sum(nums, n, left)
            return total_sum - left * (count - k)
        result = (
            sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)
        ) % mod
        return (result + mod) % mod

# Best / Most Optimal Solution
class Solution2:
    def rangeSum(self, A, n, left, right):
        B, C = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + A[i]
            C[i + 1] = C[i] + B[i + 1]
        def count_sum_under(score):
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += j - i
            return res        
        def sum_k_sums(k):
            score = kth_score(k)
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += B[j] * (j - i + 1) - (C[j] - (C[i - 1] if i else 0))
            return res - (count_sum_under(score) - k) * score
        def kth_score(k):
            l, r = 0, B[n]
            while l < r:
                m = (l + r) // 2
                if count_sum_under(m) < k:
                    l += 1
                    l = m + 1
                else:
                    r = m
            return l
        return (sum_k_sums(right) - sum_k_sums(left - 1))%(10**9+7)
