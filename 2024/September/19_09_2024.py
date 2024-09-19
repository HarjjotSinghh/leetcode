from typing import List
from functools import cache

# My Solution
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        if len(expression) == 0:
            return results
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]
        for i, current_char in enumerate(expression):
            if current_char.isdigit():
                continue
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1 :])
            for left_value in left_results:
                for right_value in right_results:
                    if current_char == "+":
                        results.append(left_value + right_value)
                    elif current_char == "-":
                        results.append(left_value - right_value)
                    elif current_char == "*":
                        results.append(left_value * right_value)
        return results

# Best / Most Optimal Solution
class Solution2:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dfs(expr):
            if len(expr) == 0:
                return []
            if expr.isnumeric():
                return [int(expr)]
            result = []
            for i, c in enumerate(expr):
                if c.isdigit():
                    continue
                left_result = dfs(expr[:i])
                right_result = dfs(expr[i+1:])
                for lr in left_result:
                    for rl in right_result:
                        match c:
                            case '+':
                                result.append(lr + rl)
                            case '-':
                                result.append(lr - rl)
                            case '*':
                                result.append(lr * rl)
            return result
        return dfs(expression)

