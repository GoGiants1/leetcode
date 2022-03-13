class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        s = math.inf
        l = 0
        m_profit = 0
        for i, v in enumerate(prices):
            if v > l:
                l = v
            
            if v < s:
                s = l = v
                
            if m_profit < l - s:
                m_profit = l - s
        
        
        return m_profit