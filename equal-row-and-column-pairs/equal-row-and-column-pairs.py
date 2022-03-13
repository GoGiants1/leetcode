# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         # n = len(grid)

#         # # compare row and col one by one
        
#         # # O(n**2) * O(n) = O(n**3)

#         # # trie ? 

#         # # hm -> key: tuple, value: [[rows], [cols]]
#         # hm_r = defaultdict(list)
#         # hm_c = defaultdict(list)
#         # for i, row in enumerate(grid):
#         #     hm_r[tuple(row)].append(i)
#         #     col = []
#         #     for j in range(n):
#         #         col.append(grid[j][i])
#         #     hm_c[tuple(col)].append(i)
#         # pairs = set()
#         # for k, v in hm_r.items():
#         #     if k in hm_c:
#         #         for i, r in enumerate(v):
#         #             for j, c in enumerate(hm_c[k]):
#         #                 pairs.add((r,c))

#         # return len(pairs)
#         pairs = 0
#         cnt = Counter(tuple(row) for row in grid)
#         for tpl in zip(*grid):
#             pairs += cnt[tpl]
#         return pairs

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a] 
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)
        
        for row in grid:
            my_trie.insert(row)
        
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)
    
        return count    