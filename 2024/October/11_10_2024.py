import heapq
from typing import List

# My Solution
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )
        next_chair = 0
        available_chairs = []
        leaving_queue = []
        for time in times:
            arrival, leave, index = time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)
            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1
            heapq.heappush(leaving_queue, (leave, current_chair))
            if index == targetFriend:
                return current_chair
        return 0

# Best / Most Optimal Solution
class Solution:
  def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
    nextUnsatChair = 0
    emptyChairs = []
    occupied = []
    for i in range(len(times)):
      times[i].append(i)
    times.sort(key=lambda x: x[0])
    for arrival, leaving, i in times:
      while len(occupied) > 0 and occupied[0][0] <= arrival:
        unsatChair = heapq.heappop(occupied)[1]
        heapq.heappush(emptyChairs, unsatChair)
      if i == targetFriend:
        return emptyChairs[0] if len(emptyChairs) > 0 else nextUnsatChair
      if len(emptyChairs) == 0:
        heapq.heappush(occupied, (leaving, nextUnsatChair))
        nextUnsatChair += 1
      else:
        emptyChair = heapq.heappop(emptyChairs)
        heapq.heappush(occupied, (leaving, emptyChair))
