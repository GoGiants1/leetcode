class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # make combination
        # check valid parenthesis
        all_par = set()
        
        def makeCombi(op: int, cl: int, path:str, st: list):
            if op == 0 and cl == 0:
                all_par.add(path)
                return
            st.append("(")
            if op:
                makeCombi(op -1, cl, path + "(", st[:])
            st.pop()
            if cl and st and st[-1] == "(":
                st.pop()
                makeCombi(op, cl - 1, path + ")", st[:])

        makeCombi(n, n, "", [])

        return list(all_par)