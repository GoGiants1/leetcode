class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # k번 연속으로 이기면 종료
        if len(arr) < k:
            return max(arr)

        q = deque(arr)
        winner = None
        loser = None
        win_cnt = 0


        while win_cnt < k:
            prev_winner = winner
            a = q.popleft()
            b = q.popleft()
            winner, loser = max(a,b), min(a,b)
            q.appendleft(winner)
            q.append(loser)
            if prev_winner == winner:
                win_cnt += 1
            else:
                prev_winner = winner
                win_cnt = 1

        return winner