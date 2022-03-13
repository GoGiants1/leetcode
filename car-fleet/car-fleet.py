class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n개의 차. 1차선, target만큼의 거리
        # pos + x * speed 가 같아지는
        n = len(position)
        if len(position) == 1:
            return 1
        flts = list(zip(position, speed))

        flts.sort(key=lambda x: -x[0])
        st = []
        for p, s in flts:
            t = (target - p) / s
            st.append(t)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)