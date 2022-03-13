
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
            people[i] = [h_i, k_i] means i^th person of height h_i and exactly k_i other people in front who have a height greater tahn or equal to h_i.
        """
        
        heap = []
        
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
            
        return result