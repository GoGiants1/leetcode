class Trie:

    def __init__(self):
       self.word = False
       self.children = {} 

    def insert(self, word: str) -> None:
        idx = 0
        node = self
        while idx < len(word):
            if word[idx] in node.children:
                node = node.children[word[idx]]
            else:
                node.children[word[idx]] = Trie()
                node = node.children[word[idx]]
            idx += 1
        node.word = True

    def search(self, word: str) -> bool:
        node = self

        for i, ch in enumerate(word):
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self

        for i, ch in enumerate(prefix):
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)