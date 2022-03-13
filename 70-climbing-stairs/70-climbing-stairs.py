class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            twos: 2가 최대로 들어갈 수 있는 개수
            
        '''
        twos = n // 2
        
        # 1로만 이루어진 경우 1개를 미리 카운트 해두기
        cnt = 1
        
        # 2를 최대 개수부터 1개인 경우까지 순회하며 계산
        for i in range(twos, 0, -1):
            # 여기서 i는 2가 들어가는 개수
            # target은 계산 후 1이 들어가는 개수를 뜻한다
            target = n
            target -= i * 2
            
            # 조합의 개수를 구하기 위해서 분자 분모를 구분하여 누적곱을 계산
            denominator = 1
            numerator = 1
            
            # 계산의 효율성을 위해서 i가 target보다 크도록 swap
            if i < target:
                i , target = target, i
            
            # 여기서 계산 최적화가 적용 n C r 의 분자 부분
            # 분모의 큰 팩토리얼과 분자의 겹치는 부분이 약분되어 사라진 상태를 생각하였음
            for num in range(target + i, i, -1):
                numerator *= num
            
            # 분모는 큰 팩토리얼이 약분되었기 떄문에 작은 숫자의 팩토리얼을 계산
            for num in range(1, target + 1):
                denominator *= num
            
            cnt += numerator // denominator
        
        return cnt