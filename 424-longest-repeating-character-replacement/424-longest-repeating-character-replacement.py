class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Find longest Repeating character with replacement
        
        Approach: Sliding Window
        '''
#         s_len = len(s)
        
#         start = end = 0 
        
#         max_len = 1
        
#         while start < s_len:
            
#             target_char = s[start]
#             end = start + 1
#             remain_replacement = k
            
#             while end < s_len:
#                 if s[end] != target_char:
#                     if remain_replacement > 0:
#                         remain_replacement -= 1
#                     else:
#                         break
#                 end += 1
                
#             if max_len < end - start:
#                 max_len = end - start
            
#             start += 1
        
        
        
#         return max_len
        
        left = right = 0
        cnts = collections.Counter()
        for right in range(1, len(s) + 1):
            cnts[s[right - 1]] += 1
            
            max_char_n = cnts.most_common(1)[0][1]
        
            if right - left - max_char_n > k:
                cnts[s[left]] -= 1
                left += 1
        
        return right - left

            