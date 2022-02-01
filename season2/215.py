import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we can use a max heap of size k to store the numbers
        # this will give us a n * log n time, and we can prune
        # that by discarding elements that are larger than the top
        # once we have a full heap, we can peak the top of the heap and
        # discard any value larger than this
        
        # by default, heap in python is a max heap
        
        heap_list = []
        
        for n in nums:
            if len(heap_list) >= k:
                if heap_list[0] < n:
                    heapq.heappushpop(heap_list, n) 
            else:
                heapq.heappush(heap_list, n)
        
        return heap_list[0]
