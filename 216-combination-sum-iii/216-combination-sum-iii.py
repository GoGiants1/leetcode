class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if ((k + 1) * k) // 2 > n:
            return []
        
        self.result =[]
        self.dfs([],1,k,n)
        return self.result
    
    def dfs(self,path,start,k,target):
        
        if k ==0 and target==0:
            self.result.append(path)
            return 
        
        if k ==0 or target==0:
            return
        
        for i in range(start,10):
            self.dfs(path+[i],i+1,k-1,target-i)