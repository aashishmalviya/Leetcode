# https://www.youtube.com/watch?v=h9iTnkgv05E
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        neighbors = defaultdict(list)
        
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
                
        visited = set()
        visited.add(beginWord)
        
        q = deque()
        q.append(beginWord)
        
        result = 1
        
        while q:
            
            qLen = len(q)
            
            for i in range(qLen):
                
                word = q.popleft()
                
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1: ]
                    
                    for current_neighbor in neighbors[pattern]:
                        if current_neighbor not in visited:
                            visited.add(current_neighbor)
                            q.append(current_neighbor)
            
            result += 1
        
        return 0