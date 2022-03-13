class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # 비트 연산 ? a'| b' = c

        def checkFlip(aa: int, bb:int, cc:int) -> int:
            flips = 0
            # flip a or flip b
            if aa | bb == cc:
                return flips
            elif (not aa) | bb == cc or aa | (not bb) == cc:
                flips += 1
            else:
                flips += 2
            return flips
        

        # 각 자리마다(2진수) mask와 각각 and 연산 후, 비교
        f = 0
        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            f += checkFlip(bit_a, bit_b, bit_c)

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return f


        