from typing import List


# My Solution
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0
        for i in range(n):
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left
            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right
        return answer


# Best / Most Optimal Solution
class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        pref = p = s = 0
        for i, el in enumerate(boxes):
            if el == "1":
                pref += i
                p += 1
        for el in boxes:
            answer.append(pref)
            if el == "1":
                p -= 1
                s += 1
            pref = pref - p + s
        return answer
