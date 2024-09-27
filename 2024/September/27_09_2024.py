from sortedcontainers import SortedDict
import bisect

# My Solution
class MyCalendarTwo:
    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2
    def book(self, start: int, end: int) -> bool:
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1
        overlapped_booking = 0
        for count in self.booking_count.values():
            overlapped_booking += count
            if overlapped_booking > self.max_overlapped_booking:
                self.booking_count[start] -= 1
                self.booking_count[end] += 1
                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                return False
        return True

# Best / Most Optimal Solution
class MyCalendarTwo:
    def __init__(self):
        self.single_booked = []
        self.double_booked = []
    def intersection(self, intervals, s, e):
        l = bisect.bisect_left(intervals, s)
        r = bisect.bisect_right(intervals, e)
        intersection = []
        if l % 2:
            if intervals[l] != s:
                intersection.append(s)
            else:
                l = l + 1
        intersection += intervals[l:r]
        if r % 2:
            if intervals[r-1] != e:
                intersection.append(e)
            else:
                intersection.pop()
        return intersection
    def add(self, intervals, s, e):
        l = bisect.bisect_left(intervals, s)
        r = bisect.bisect_right(intervals, e)
        new = []
        if not l % 2:
            new.append(s)
        if not r % 2:
            new.append(e)
        intervals[l:r] = new
    def book(self, start: int, end: int) -> bool:
        if self.intersection(self.double_booked, start, end):
            return False
        intersection = self.intersection(self.single_booked, start, end)
        if intersection:
            for i in range(len(intersection) // 2):
                i1 = intersection[2*i]
                i2 = intersection[2*i+1]
                self.add(self.double_booked, i1, i2)
        self.add(self.single_booked, start, end)
        return True
