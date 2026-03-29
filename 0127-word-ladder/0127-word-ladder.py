from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        wordSet = set(wordList)
        
        # if endWord not present → impossible
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        visited = set([beginWord])
        steps = 1
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return steps
                
                # try all 1-letter transformations
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i+1:]
                        
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            
            steps += 1
        
        return 0