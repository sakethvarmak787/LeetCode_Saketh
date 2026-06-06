class MyCalendar:

    def __init__(self):
        self.meetings = []

    def book(self, start: int, end: int) -> bool:

        for s, e in self.meetings:

            if start < e and end > s:
                return False

        self.meetings.append((start, end))
        return True