class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_cnt = collections.Counter(arr)
        
        cnts = list(list(zip(*num_cnt.most_common()))[1])
        
        set_cnts = list(set(cnts))
        
        if(len(set_cnts) == len(cnts)):
            return True
        else:
            return False