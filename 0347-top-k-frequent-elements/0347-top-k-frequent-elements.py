class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums) # O(n)
        # use heap to pop the smallest automatically
        import heapq
        container = []
        for elm, freq in h.items():
            if len(container)<k:
                # O(log k)
                # heap keep the smallest pair at root according to pair's first element
                # so place freq at first
                heapq.heappush(container, (freq, elm))
            else:
                heapq.heappushpop(container, (freq, elm)) 
        return [elm for freq, elm in container]
