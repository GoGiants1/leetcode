class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        from pprint import pprint
        # n combination 2
        # Maybe O(n**2) time cplx
        
        # Key: first letter
        # value: full name
        # ord와 chr !!! 
        pre_to_suf = defaultdict(set)
        out = 0
        for idea in ideas:
            pre_to_suf[ord(idea[0])-ord("a")].add(idea[1:])
        # pprint(pre_to_suf)
        alpha_len = ord('z') - ord('a') + 1
        for i in range(alpha_len):
            for j in range(i + 1, alpha_len):
                if i in pre_to_suf and j in pre_to_suf:
                    
                    intersection_len = len(pre_to_suf[i] & pre_to_suf[j])
                    # print(i, j, pre_to_suf[i], pre_to_suf[j])
                    out += 2 * (len(pre_to_suf[i]) - intersection_len) * (len(pre_to_suf[j]) - intersection_len)
        return out