class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            alp = node.children.get(c, None)
            if alp is None:
                alp = node.children[c] = TrieNode()
            node = alp
        node.word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        def search_in_node(word:str, node: TrieNode) -> bool:
            for i, c in enumerate(word):
                if c in node.children:
                    node = node.children[c]
                else:
                    if c == ".":
                        for x in node.children:
                            if search_in_node(word[i + 1:], node.children[x]):
                                return True
                    return False
            return node.word
        return search_in_node(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)