class Trie:

    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        self.prefixes.add(word)
        for i, _ in enumerate(word):
            if i > 0:
                self.prefixes.add(word[:i])

    def search(self, word: str) -> bool:
        return True if word in self.words else False

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.prefixes else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)