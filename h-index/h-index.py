class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = Counter(citations)
        n = len(citations)

        acc = 0
        k = sorted(list(cnt.keys()), reverse=True)
        key = -1
        for key in k:
            if key > 0:
                acc += cnt[key]
                if acc == key:
                    return key
                elif acc > key:
                    prev = acc - cnt[key]
                    if prev > key:
                        return prev
                    else:
                        return key
                        
        return acc