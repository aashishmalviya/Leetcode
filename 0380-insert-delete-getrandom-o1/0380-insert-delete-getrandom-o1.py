class RandomizedSet:

    def __init__(self):
        self.valArray = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.indexMap[val] = len(self.valArray)
        self.valArray.append(val);
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        targetIndex = self.indexMap[val]
        self.valArray[targetIndex] = self.valArray[-1]
        self.indexMap[self.valArray[-1]] = targetIndex
        del self.indexMap[val]
        self.valArray.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.valArray)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()