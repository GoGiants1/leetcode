class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # memo = defaultdict(list)
        # if len(strs) < 2:
        #     return [strs]

        # for i, v in enumerate(strs):
        #     k = sorted(v)
        #     memo["".join(k)].append(v)
            
        # out = []
        # for k in memo:
        #     out.append(memo[k])
        # return out

        memo = defaultdict(list)

        def makeKeyVal(s: str) -> (str, str):
            # a to z
            key = [0] * 26
            base = ord('a')
            for v in s:
                key[ord(v)-base] += 1
            
            return (tuple(key), s)

        
        for i, v in enumerate(strs):
            key, val = makeKeyVal(v)
            memo[key].append(val)
        out = []
        for k in memo:
            out.append(memo[k])
        return out
        
