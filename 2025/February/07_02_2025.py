from typing import List


# My Solution
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        b_colors = {}
        col_count = {}
        dis_colors = set()
        res = []
        for x, y in queries:
            if x in b_colors:
                old_color = b_colors[x]
                col_count[old_color] -= 1
                if col_count[old_color] == 0:
                    dis_colors.remove(old_color)
            b_colors[x] = y
            if y in col_count:
                col_count[y] += 1
            else:
                col_count[y] = 1
            dis_colors.add(y)
            res.append(len(dis_colors))
        return res


# Best / Most Optimal Solution
class Solution2:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        distinct = 0
        ball_color = {}
        color_count = {}
        for ball, new_color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
                    distinct -= 1
            ball_color[ball] = new_color
            if new_color in color_count:
                color_count[new_color] += 1
            else:
                color_count[new_color] = 1
                distinct += 1
            res.append(distinct)
        return res
