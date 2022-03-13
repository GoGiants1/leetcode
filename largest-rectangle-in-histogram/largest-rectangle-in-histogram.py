class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        st = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                max_area = max((i - index) * height, max_area)
                start = index
            st.append((start, h))
        
        for i, h in st:
            max_area = max((len(heights)-i) * h, max_area)
        return max_area

