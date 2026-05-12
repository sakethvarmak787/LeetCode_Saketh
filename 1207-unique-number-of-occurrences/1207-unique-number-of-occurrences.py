class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        res = []    

        for value in count_dict.values():
            res.append(value)

        if len(res) != len(set(res)):
            return False
        else:
            return True
