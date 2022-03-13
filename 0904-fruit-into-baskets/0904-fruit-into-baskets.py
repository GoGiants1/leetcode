class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        q = deque()
        cnt = defaultdict(int)
        out = 0
        # deque and hashmap
        for i, v in enumerate(fruits):
            q.append(v)
            cnt[v] += 1
            if len(cnt.keys()) == 2:
                out = max(out, len(q))
            while q and len(cnt.keys()) > 2:
                popped = q.popleft()
                cnt[popped] -= 1
                if cnt[popped] == 0:
                    del cnt[popped]
        if len(cnt.keys()) < 3:
            out = max(out, len(q))
        return out