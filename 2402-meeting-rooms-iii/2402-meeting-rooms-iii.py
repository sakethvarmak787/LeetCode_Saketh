import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        count = [0] * n

        available = [i for i in range(n)]
        heapq.heapify(available)

        busy = []

        for start, end in meetings:

            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:

                room = heapq.heappop(available)

                count[room] += 1

                heapq.heappush(busy, (end, room))

            else:

                duration = end - start

                end_time, room = heapq.heappop(busy)

                count[room] += 1

                heapq.heappush(
                    busy,
                    (end_time + duration, room)
                )

        max_meetings = max(count)

        for room in range(n):
            if count[room] == max_meetings:
                return room