class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        
        num_to_idx = collections.defaultdict(list)
        
        for i, v in enumerate(arr):
            num_to_idx[v].append(i)
            
        tuples = []
        
        if len(keys) == 1:
            z_len = arr.count(keys[0])
            return ((z_len * (z_len -1) * (z_len - 2)) // 6) % (10**9 + 7)
        
        
        while keys:
            c = keys.pop()
            if c > target:
                continue
            remain = target - c
            for a in keys:
                b = remain - a
                
                if b < a:
                    break
                
                if b in keys:
                    if b == a and len(num_to_idx[b]) == 1:
                        continue
                    tuples.append((a,b,c))
    
            if 2 * c <= target and target - 2 * c in keys:
                if len(num_to_idx[c]) > 1:
                    tuples.append((target - 2 * c, c, c))

                
        ans = 0
        
        for a, b, c in tuples:
            l_a, l_b, l_c = len(num_to_idx[a]), len(num_to_idx[b]), len(num_to_idx[c])
            if a == b == c:
                l_b -= 1
                l_c -= 2
                ans += (l_a * l_b * l_c) // 6

            elif a == b or b != c:
                l_b -= 1
                ans += (l_a * l_b * l_c) // 2
            else:
                ans += (l_a * l_b * l_c) 
        
        return ans % (10 ** 9 + 7)
        """
        
    
        
        c = collections.Counter(arr)
        res = 0
        # 중복 허용하여 선택, 정렬된 순서로 나옴
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k:
                res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j:
                res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)
        
    