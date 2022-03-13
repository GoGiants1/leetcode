class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adjacent = defaultdict(list)
        for i, w in enumerate(wordList):
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                adjacent[pattern].append(w)

        q = deque()
        q.append((beginWord, 1))
        seen = set()
        seen.add(beginWord)

        while q:
            curr_str, step = q.popleft()
            if curr_str == endWord:
                return step
            for i in range(len(curr_str)):
                pattern = curr_str[:i] + "*" + curr_str[i+1:]
                for nei in adjacent[pattern]:
                    if nei not in seen:
                        q.append((nei, step + 1))
                        seen.add(nei)

        return 0