class Solution:
    def candy(self, ratings: List[int]) -> int:
        # n 명의 아이들, 줄 서있음
        n = len(ratings)
        candy_cnt = 0
        l = [1] * n
        r = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                l[i] = l[i-1] + 1
            if ratings[-i-1] > ratings[-i]:
                r[-i-1] = r[-i] + 1
        print(l,r)
        for i in range(n):
            candy_cnt += max(l[i], r[i])
        
        return candy_cnt