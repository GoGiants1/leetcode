class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 무제한 보트
        # 최대 중량 limit
        # boat can carries max 2 people
        # DP problem ? 
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
