class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_ending_here = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_words(self, word: str):
        current_node = self.root

        for c in word:
            current_node = current_node.children[c]

        current_node.is_ending_here = True

    def is_word_present(self, word: str) -> bool:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]

        return current_node.is_ending_here

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        my_trie = Trie()

        my_trie.add_words(word)

        rows = len(board)
        cols = len(board[0])

        # test = Trie()
        # test.add_words(word)
        
        # for c in word:
        #     if c not in test.root.children:
        #         print (c + "not found in trie")
        #     test.root = test.root.children[c]
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and self.dfs_helper(board, i, j, my_trie.root) == True:
                    return True

        return False

    def dfs_helper(self, board, i, j, current_node) -> bool:
        if current_node.is_ending_here == True:
            return True

        rows = len(board)
        cols = len(board[0])

        if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in current_node.children:
            return False

        current_char = board[i][j]
        board[i][j] = '#'

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        for x,y in directions:
            new_i = i + x
            new_j = j + y

            if (self.dfs_helper(board, new_i, new_j, current_node.children[current_char]) == True):
                return True

        board[i][j] = current_char
        return False