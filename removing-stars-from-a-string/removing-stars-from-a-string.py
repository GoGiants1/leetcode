class Solution:
    def removeStars(self, s: str) -> str:
        q = []

        for i, v in enumerate(s):
            if v == "*":
                q.pop()
            else:
                q.append(v)
        
        return "".join(q)