class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search using python built-in function (my sol 1)
        # from bisect import bisect
        # idx = bisect(letters,target)
        # if idx >= len(letters):
        #     return letters[0]
        # return letters[idx]

        # my sol 2. impl bin search
        left = 0
        right = len(letters) - 1
    
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]