class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
            Args:
                g: greedy factors -> ith child want at least g[i] cookie
                s: 
                    s[j]: jth cookie size
            Returns:
                satisfied children number
        """
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()
        g_q = collections.deque(g)
        s_q = collections.deque(s)


        while g_q and s_q:
            greedy = g_q.popleft()
            cookie = s_q.popleft()
            if greedy > cookie:
                g_q.appendleft(greedy)
                

        return len(g) - len(g_q)