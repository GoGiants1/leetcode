class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(s) != len(goal):
            return False
        for shift, v in enumerate(s):
            shifted = s[shift:] + s[:shift]
            if hash(shifted) == hash(goal) and shifted == goal:
                return True
        return False