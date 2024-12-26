from collections import deque


# My Solution
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for curr_char in expression:
            if curr_char == "," or curr_char == "(":
                curr_char
            if curr_char in ["t", "f", "!", "&", "|"]:
                st.append(curr_char)
            elif curr_char == ")":
                has_true = False
                has_false = False
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")
        return st[-1] == "t"


# Best / Most Optimal Solution
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(
                    all(seen)
                    if operator == "&"
                    else any(seen) if operator == "|" else not seen.pop()
                )
            elif c != ",":
                stack.append(True if c == "t" else False if c == "f" else c)
        return stack.pop()
