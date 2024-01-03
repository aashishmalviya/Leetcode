from heapq import heappush, heappop, heappushpop
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_max_heap) == len(self.right_min_heap):
            heappush(self.right_min_heap, -heappushpop(self.left_max_heap, -num))
        else:
            heappush(self.left_max_heap, -heappushpop(self.right_min_heap, num))

    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (self.right_min_heap[0] - self.left_max_heap[0]) / 2.0
        else:
            return self.right_min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()