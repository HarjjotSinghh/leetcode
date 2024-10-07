
# My Solution
class Solution:
    def minLength(self, s: str) -> int:
        char_list = list(s)
        write_ptr = 0
        for read_ptr in range(len(s)):
            char_list[write_ptr] = char_list[read_ptr]
            if (
                write_ptr > 0
                and char_list[write_ptr - 1] in "AC"
                and ord(char_list[write_ptr])
                == ord(char_list[write_ptr - 1]) + 1
            ):
                write_ptr -= 1
            else:
                write_ptr += 1
        return write_ptr

# Best / Most Optimal Solution
class Solution:
    def minLength(self, s: str) -> int:
        s1=[]
        for p in s:
            if(s1 and((s1[-1]=="A" and p=="B") or(s1[-1]=="C" and p=="D"))):
                s1.pop()
            else:
                s1.append(p)
        return (len(s1))
