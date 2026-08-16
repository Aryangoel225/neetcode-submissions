class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_tasks = defaultdict(int) # tasks: freq
        # in a hashmap of freq show the values
        # loop through the task array
        for task in tasks:
            freq_tasks[task] += 1
        
        # create a maxheap 
        heap = [-count for count in freq_tasks.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                # pop the largest count, decrement it
                # if it still has work left, push (count, time + n) onto the queue
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    queue.append((count, time + n))  
            else:
                time = queue[0][1]   # fast-forward through idle slots
            if queue and queue[0][1] == time:
                count, queue_time = queue.popleft()
                heapq.heappush(heap, count)
        return time
                