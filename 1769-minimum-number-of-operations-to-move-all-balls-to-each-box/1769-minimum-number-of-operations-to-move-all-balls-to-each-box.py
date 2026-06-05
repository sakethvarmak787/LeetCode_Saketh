class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = [0] * len(boxes)

        take = []

        for i, ch in enumerate(boxes):
            if ch == "1":
                take.append(i)

        for i in range(len(boxes)):

            for pos in take:
                answer[i] += abs(i - pos)

        return answer