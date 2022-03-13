class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(["+", "-", "*", "/"])

        def doOps(a:int, b:int, ops: str):
            out = None
            if ops == "+":
                out = a + b
            elif ops == "-":
                out = a - b
            elif ops == "*":
                out = a * b
            else:
                if (b > 0 and a > 0) or (a < 0 and b < 0):
                    out = a // b
                else:
                    out = -(abs(a) // abs(b))
                
            return str(out)

        st = []
        for i, v in enumerate(tokens):
            if v in op:
                b = st.pop()
                a = st.pop()
                st.append(doOps(int(a) , int(b) , v))
            else:
                st.append(v)
        return int(st[-1])