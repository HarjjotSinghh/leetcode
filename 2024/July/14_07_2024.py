import re
from collections import defaultdict

# My Solution
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        matcher.reverse()
        final_map = defaultdict(int)
        stack = [1]
        running_mul = 1
        for atom, count, left, right, multiplier in matcher:
            if atom:
                if count:
                    final_map[atom] += int(count) * running_mul
                else:
                    final_map[atom] += 1 * running_mul
            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                running_mul *= multiplier
                stack.append(multiplier)
            elif left:
                running_mul //= stack.pop()
        final_map = dict(sorted(final_map.items()))
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans
    
            
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula):
            stack = [defaultdict(int)]
            i, n = 0, len(formula)
            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[start:i] or 1)
                    top = stack.pop()
                    for elem, cnt in top.items():
                        stack[-1][elem] += cnt * multiplier
                else:
                    start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[start:i]
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)
                    stack[-1][elem] += count
            return stack[0]
        element_counts = parse_formula(formula)
        sorted_elements = sorted(element_counts.items())
        result = []
        for elem, count in sorted_elements:
            result.append(elem)
            if count > 1:
                result.append(str(count))
        return ''.join(result)
