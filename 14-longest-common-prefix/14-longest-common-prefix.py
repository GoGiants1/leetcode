class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find strs length
        len_list = [len(s) for s in strs]
        min_len = min(len_list)
        n = len(strs)
        
        common_prefix = []
        for i in range(min_len):
            common_set = {}
            
            for j in range(n):
                common_set[strs[j][i]] = 1
            
            if len(common_set.keys()) == 1:
                common_prefix.append(*common_set.keys())
            else:
                break
        return ''.join(common_prefix)
                