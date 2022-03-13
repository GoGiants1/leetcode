class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # q = deque()
        # is_dup = set()
        # deleted = 0
        # for i, v in enumerate(nums):
        #     if v in is_dup:
        #         q.append(i)
        #         deleted += 1
        #     else:
        #         if q:
        #             idx = q.popleft()
        #             nums[idx] = v
        #             q.append(i)
        #         is_dup.add(v)
        # return len(nums) - deleted
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex