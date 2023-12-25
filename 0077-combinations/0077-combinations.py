class Solution:
    def __init__(self):
        self.temp_list = []
        self.result = []
        
    def combine(self, n: int, k: int) -> List[List[int]]:       
        def combination_populator(start: int, n: int, k: int):
            if len(self.temp_list) == k:
                self.result.append(self.temp_list[:])
                # print(self.result)
                return

            for i in range(start, n+1):
                self.temp_list.append(i)
                combination_populator(i+1, n, k)
                del self.temp_list[-1]

        combination_populator(1, n, k)
        return self.result