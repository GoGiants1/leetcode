class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # DFS, BFS ?
        # DP?
        # 전략: 
        # 1. ocurrence 를 두 단어에서 파악
        # 1-2. 파악한 key 값이 동일한지 확인, 다르면 false
        # 2. ocurrence 동일하게 재배치
        # 3. 실패시 false return
        
        from collections import Counter
        
        cnt_1 = Counter(word1)
        cnt_2 = Counter(word2)
        
        if set(cnt_1.keys()) != set(cnt_2.keys()):
            return False
        
        if sorted(cnt_1.values()) != sorted(cnt_2.values()):
            return False
        
        return True
    
# a-3, b-4, c-2, d-2, e-5, f-5
# a-5, b-2, c-3, d-3, e-4, f-4