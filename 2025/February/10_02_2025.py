# My Solution
class Solution:
    def clearDigits(self, s: str) -> str:
        answer = []
        for char in s:
            if char.isdigit() and answer:
                answer.pop()
            else:
                answer.append(char)
        return "".join(answer)


# Best / Most Optimal Solution
class Solution2:
    def clearDigits(self, s: str) -> str:
        letters = []
        letters_to_delete = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i].isnumeric():
                letters_to_delete += 1
            else:
                if letters_to_delete > 0:
                    letters_to_delete -= 1
                else:
                    letters.append(s[i])
        letters.reverse()
        return "".join(letters)
