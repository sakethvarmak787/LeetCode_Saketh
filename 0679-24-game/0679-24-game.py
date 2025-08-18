import itertools
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def apply_operations(a, b):
            results = []
            results.append(a + b)
            results.append(a - b)
            results.append(b - a)
            results.append(a * b)
            if b != 0:
                results.append(a / b)
            if a != 0:
                results.append(b / a)
            return results

        def new_lists(cards, a, b):
            results = []
            for val in apply_operations(a, b):
                new_cards = cards[:]
                new_cards.remove(a)
                new_cards.remove(b)
                new_cards.append(val)
                results.append(new_cards)
            return results

        def solve(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) < 1e-6
            for a, b in itertools.combinations(cards, 2):
                for new_card_list in new_lists(cards, a, b):
                    if solve(new_card_list):
                        return True
            return False

        return solve(cards)
