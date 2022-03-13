class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        r_3 = r_5 = None
        out = []
        for i in range(1, n + 1):
            r_3, r_5 = i % 3, i % 5
            
            if r_3 == 0 and r_5 == 0:
                out.append("FizzBuzz")
            elif r_3 == 0:
                out.append("Fizz")
            elif r_5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out
            
            