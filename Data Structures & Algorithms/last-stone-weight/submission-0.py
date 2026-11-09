class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap, pop two elements off the heap and if x == y, continue without reinserting (destroying both stones)
        # if x < y, subtract the two and insert back into the heap

        # initialize max heap
        heap = [-s for s in stones]
        heapq.heapify(heap)
        print(heap) # [-6, -4, -2, -2, -3]

        while len(heap) > 1:
            x, y= heapq.heappop(heap), heapq.heappop(heap)
            # have to do the opposite since it's a max heap of negative values, that's why we do x-y instead of y-x
            if x != y: 
                heapq.heappush(heap, x-y)
        
        return -heap[0] if heap else 0