#https://leetcode.com/problems/word-search-ii/discuss/1511657/Python-clean-with-Trie-pruning-optimization-and-code-comments

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_ending_node = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str):
        current_node = self.root
        for c in word:
            current_node = current_node.children[c]

        current_node.is_ending_node = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        my_trie = Trie()

        for word in words:
            my_trie.add_word(word)

        rows = len(board)
        cols = len(board[0])

        result = []

        for i in range(rows):
            for j in range(cols):
                words_found = []
                current_word = ""
                self.dfs_helper(board, i, j, my_trie.root, current_word, words_found)
                result += words_found

        return result

    def dfs_helper(self, board, i, j, current_node, current_word, words_found):
        if current_node.is_ending_node:
            words_found.append(current_word)
            # set to False so not to repeat the same word
            current_node.is_ending_node = False

        rows, cols = len(board), len(board[0])

        if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in current_node.children:
            return

        current_char = board[i][j]
        board[i][j] = '#'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x,y in directions:
            new_i = i + x
            new_j = j + y
            self.dfs_helper(board, new_i, new_j, current_node.children[current_char], current_word + current_char, words_found)

        board[i][j] = current_char


        # pruning: if it is a leaf and a matched word is found for it already, pop it to decrease trie size
        if len(current_node.children[current_char].children) == 0:
            del current_node.children[current_char]

