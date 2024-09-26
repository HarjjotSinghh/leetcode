from sortedcontainers import SortedList

# My Solution
class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()
    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True

# Best / Most Optimal Solution

class MyCalendar:
    def __init__(self):
        self.bookings = [ (-1,-1), (float('inf'), float('inf')) ]
    def book(self, start: int, end: int) -> bool:
        index = bisect_left(self.bookings, (start, end))
        if start < self.bookings[index - 1][1]:
            return False
        if end > self.bookings[index][0]:
            return False
        self.bookings.insert(index, (start, end))
        return True

