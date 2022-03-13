class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
            deque 에 넣고 # 나오면 pop()
        """
        s_dq = collections.deque()
        t_dq = collections.deque()
        s_len = len(s)
        t_len = len(t)
        max_len = max(s_len, t_len)
        for i in range(max_len):
            s_can_write = True
            t_can_write = True
            
            if i < s_len and s[i] == '#':
                if len(s_dq):
                    s_dq.pop()
                s_can_write = False
            if i < t_len and t[i] == '#':
                if len(t_dq):
                    t_dq.pop()
                t_can_write = False
                
            
            if not (s_can_write or t_can_write):
                continue
            
            if i < s_len and s_can_write:
                s_dq.append(s[i])
            if i < t_len and t_can_write:
                t_dq.append(t[i])
        print(s_dq, t_dq)
        return list(s_dq) == list(t_dq)
            
            