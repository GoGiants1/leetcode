class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            Arguments:
                tasks: alphabet task list that CPU needs to do
                n: cooldown period between same tasks

            Returns:
                least number of units of times that CPU will take to finish all given tasks
                총 소요시간.
        """
        
        '''brute force method -> time out
        cooldown_q = collections.deque()

        cnt = collections.Counter(tasks)

        time = 0

        while cnt:
            if len(cooldown_q) == n+1:
                cooldown_q.popleft()
            executed = None
            for t, _ in cnt.most_common(n + 1):
                if not t in cooldown_q:
                    executed = t
                    cnt.subtract(t)
                    cnt += collections.Counter()
                    break

            cooldown_q.append(executed)
            time += 1

        return time
        '''
        '''
        res = 0
        cnt = collections.Counter(tasks)
        while True:
            sub_tasks = 0

            for t, _ in cnt.most_common(n + 1):
                sub_tasks += 1
                res += 1
                cnt.subtract(t)
                cnt += collections.Counter()
            
            if not cnt:
                break
            res += n - sub_tasks + 1
        
        return res
        '''
        # tasks = ["A","A","A","B","B","B"]
        # n = 2 
        
        counts = list(collections.Counter(tasks).values()) # [3,3]
        max_count = max(counts) # 3
        num_of_chars_with_max_count = counts.count(max_count) # 2, A and B
        
        num_of_chunks_with_idles = max_count - 1 # 2 -> A  A  A

        # either a task will fill an empty place or the place stays idle, 
        # either way the chunk size stays the same  
        length_of_a_chunk_with_idle = n + 1  # 3 -> A _ _ A _ _ A 

        # on the final chunk, there will only be most frequent letters 
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk # 2*3 + 2 = 8 
        # -> A B _ A B _ A B 

        return max(len(tasks), length_of_all_chunks)     