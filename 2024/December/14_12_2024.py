from typing import List
from collections import deque

# My Solution
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        right = left = 0
        window_len = total = 0
        cur_min = cur_max = nums[right]
        for right in range(len(nums)):
            cur_min = min(cur_min, nums[right])
            cur_max = max(cur_max, nums[right])
            if cur_max - cur_min > 2:
                window_len = right - left
                total += window_len * (window_len + 1) // 2
                left = right
                cur_min = cur_max = nums[right]
                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    cur_min = min(cur_min, nums[left])
                    cur_max = max(cur_max, nums[left])
                if left < right:
                    window_len = right - left
                    total -= window_len * (window_len + 1) // 2
        window_len = right - left + 1
        total += window_len * (window_len + 1) // 2
        return total

# Best / Most Optimal Solution
class Solution2:
    def continuousSubarrays(self, nums: List[int]) -> int:
        q1 = deque()
        q2 = deque()
        q3 = deque()
        ans = 1
        l = 1
        k = nums[0]
        q1.append(0)
        for i in range(1, len(nums)):
            n = nums[i]
            if k <= n <= k + 2:
                l += 1
                ans += l
                if n == k:
                    q1.append(i)
                elif n == k + 1:
                    q2.append(i)
                else:
                    q3.append(i)
            elif n < k - 2 or n > k + 4:
                q1 = deque()
                q2 = deque()
                q3 = deque()
                q1.append(i)
                l = 1
                ans += 1
                k = n
            elif n == k - 1:
                start = 0 if len(q3) == 0 else q3[-1]
                while len(q1) != 0 and q1[0] < start: q1.popleft()
                while len(q2) != 0 and q2[0] < start: q2.popleft()
                q3 = q2
                q2 = q1
                q1 = deque()
                q1.append(i)
                l = len(q2) + len(q3) + 1
                ans += l
                k = n
            elif n == k - 2:
                start = 0 if len(q3) == 0 else q3[-1]
                start = start if len(q2) == 0 or (q2[-1] < start) else q2[-1]
                while len(q1) != 0 and q1[0] < start: q1.popleft()
                q3 = q1
                q2 = deque()
                q1 = deque()
                q1.append(i)
                k = n
                l = len(q3) + 1
                ans += l
            elif n == k + 3:
                start = 0 if len(q1) == 0 else q1[-1]
                while len(q2) != 0 and q2[0] < start: q2.popleft()
                while len(q3) != 0 and q3[0] < start: q3.popleft()
                if len(q2) == 0:
                    if len(q3) == 0:
                        q1 = deque()
                        q2 = deque()
                        q3 = deque()
                        q1.append(i)
                        l = 1
                        ans += 1
                        k = n
                    else:
                        q1 = q3
                        q2 = deque()
                        q3 = deque()
                        q2.append(i)
                        l = len(q1) + 1
                        ans += l
                        k = n-1
                else:
                    q1 = q2
                    q2 = q3
                    q3 = deque()
                    q3.append(i)
                    l = len(q1) + len(q2) + 1
                    ans += l
                    k = n - 2
            else:
                start = 0 if len(q1) == 0 else q1[-1]
                start = start if len(q2) == 0 or (q2[-1] < start) else q2[-1]
                while len(q3) != 0 and q3[0] < start: q3.popleft()
                if len(q3) == 0:
                    q1 = deque()
                    q2 = deque()
                    q3 = deque()
                    q1.append(i)
                    l = 1
                    ans += 1
                    k = n
                else:
                    q1 = q3
                    q2 = deque()
                    q3 = deque()
                    q3.append(i)
                    k = n - 1
                    l = len(q1) + 1
                    ans += l
        return ans