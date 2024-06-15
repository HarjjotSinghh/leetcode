from typing import List

class Solution:
    # My Solution
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], 
                                         capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(capital, profits),
                                       key=lambda x: x[0], reverse=True)
        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heappush(heap, -projects.pop()[1])
            if heap: w-= heappop(heap)
        return w


# Optimal/Best Solution
def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    if w > max(capital):
        return w + sum(nlargest(k, profits))
    maxProfit = []
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    heapify(minCapital)
    for i in range(k):
        while minCapital and minCapital[0][0] <= w :
            c, p = heappop(minCapital)
            heappush(maxProfit, -1 * p)
        if not maxProfit :
            break
        w += -1 * heappop(maxProfit)
    return w
if __name__ =='__main__' :
    with open('user.out', 'w') as f :
        for k, w, profits, capital in zip(map(loads, stdin), map(loads, stdin), map(loads, stdin), map(loads, stdin)) :
            print(findMaximizedCapital(k, w, profits, capital), file = f)
    exit()