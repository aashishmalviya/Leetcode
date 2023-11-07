class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            requested_value = self.cache[key]
            self.cache.move_to_end(key)
            return requested_value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.maxCapacity:
                self.cache.popitem(last = False)
        
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)