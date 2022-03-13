class Solution:
    def decodeString(self, s: str) -> str:
        def getString(sub:str, rpt):
            if rpt is None:
                rpt = 1
            
            return sub * rpt
        nums = set(str(i) for i in range(10))
        op = cl = 0
        repeat = None
        n_s = []
        stack = []
        out = []
        for i, v in enumerate(s):
            # print(i, v, s, stack, out, repeat)
            if v in nums:
                if op == 0:
                    n_s.append(v)
                else:
                    stack.append(v)
            elif v == "[":
                op += 1
                if op == 1:
                    try:
                        repeat = int("".join(n_s))
                    except:
                        repeat = 1
                    
                    continue
                stack.append(v)

            elif v == "]":
                cl += 1
                if op == cl:
                    out.append(getString(self.decodeString("".join(stack)), repeat))
                    op = cl = 0
                    stack = []
                    repeat = None
                    n_s = []
                else:
                    stack.append(v)
            else:
                if repeat is None:
                    out.append(v)
                else:
                    stack.append(v)
       
        
        return getString("".join(out), repeat)

        






            
            

