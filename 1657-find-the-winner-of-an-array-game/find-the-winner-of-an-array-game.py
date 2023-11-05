class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # k번 연속으로 이기면 종료
        curr = arr[0]
        max_el = max(arr)
        win_cnt = 0
        for i in range(1, len(arr)):
            opponent = arr[i]
            if curr > opponent:
                win_cnt += 1
            else:
                win_cnt = 1
                curr = opponent
                
            if win_cnt == k:
                return curr
            if curr == max_el:
                return curr

            