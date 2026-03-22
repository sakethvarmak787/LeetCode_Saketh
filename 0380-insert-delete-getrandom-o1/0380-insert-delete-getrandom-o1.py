import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False
        
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        
        idx = self.map[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.map[last] = idx

        self.arr.pop()
        del self.map[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)