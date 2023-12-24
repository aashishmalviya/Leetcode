from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_ending_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for c in word:
            current_node = current_node.children[c]

        current_node.is_ending_node = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)

    def search_helper(self, word: str, node: TrieNode, i = 0) -> bool:

        if not node:
            return False

        if i == len(word):
            return node.is_ending_node

        if word[i] == '.':
            return any((self.search_helper(word, child, i+1) for child in node.children.values()))

        return self.search_helper(word, node.children.get(word[i], None), i+1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)