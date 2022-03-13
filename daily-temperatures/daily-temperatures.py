class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # heapq?
        out = [0] * len(temperatures)
        st = []
        for i, v in enumerate(temperatures):
            while st and st[-1][0] < v:
                tmp, idx = st[-1]
                out[idx] = i - idx
                st.pop()
            st.append((v,i))
        return out
