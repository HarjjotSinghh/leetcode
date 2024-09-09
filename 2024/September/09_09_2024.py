from typing import List
import sys
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        i = 0
        j = 0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]
        while head is not None:
            res[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]
            if (
                min(newi, newj) < 0
                or newi >= m
                or newj >= n
                or res[newi][newj] != -1
            ):
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]
            head = head.next
        return res

# Best / Most Optimal Solution
class Solution2:
    def spiralMatrix(self, rows: int, columns: int, head: ListNode) -> list[list[int]]:
        matrix = [[-1] * columns for _ in range(rows)]
        topRow, bottomRow = 0, rows - 1
        leftColumn, rightColumn = 0, columns - 1
        while head:
            for col in range(leftColumn, rightColumn + 1):
                if head:
                    matrix[topRow][col] = head.val
                    head = head.next
            topRow += 1
            for row in range(topRow, bottomRow + 1):
                if head:
                    matrix[row][rightColumn] = head.val
                    head = head.next
            rightColumn -= 1
            for col in range(rightColumn, leftColumn - 1, -1):
                if head:
                    matrix[bottomRow][col] = head.val
                    head = head.next
            bottomRow -= 1
            for row in range(bottomRow, topRow - 1, -1):
                if head:
                    matrix[row][leftColumn] = head.val
                    head = head.next
            leftColumn += 1
        return matrix
def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'
def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines) // 3
    results = []
    for i in range(num_test_cases):
        m = int(lines[i*3])
        n = int(lines[i*3 + 1])
        head_values = json.loads(lines[i*3 + 2])
        if not head_values:
            head = None
        else:
            head = ListNode(head_values[0])
            current = head
            for value in head_values[1:]:
                current.next = ListNode(value)
                current = current.next
        result = Solution().spiralMatrix(m, n, head)
        formatted_result = format_output(result)
        results.append(formatted_result)
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    kdsmain()
    exit(0)
