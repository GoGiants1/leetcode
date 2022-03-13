class Solution:
    def romanToInt(self, s: str) -> int:
        '''
            I, X, C 예외 케이스 유의하기
        '''
        romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        vals = [1,5,10,50,100,500,1000]
        
        roman2num = {}
        
        for r, v in list(zip(romans, vals)):
            roman2num[r] = v
            
        can_be_prefix = [1, 10, 100]
        
        before_val = 0
        acc = 0
        
        for i, roman in enumerate(s):
            if before_val <  roman2num[roman]:
                if before_val in can_be_prefix:
                    acc -= 2 * before_val
            acc +=  roman2num[roman]
            before_val =  roman2num[roman]
        
        return acc 
            
            