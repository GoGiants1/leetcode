class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 최소 2개의 원소
        # 원소 합이 k의 배수가 나와야함.
        # 슬라이딩 윈도우? 투 포인터?
        # 0도 정답으로 처리 -> k로 나눠서 나머지 0인지 확인
        # 생각 잘 안나면 해시맵!!!! -> 딕셔너리
        
        hash_map = {0: 0}
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
                
            elif hash_map[s % k] < i:
                    return True
        
        return False