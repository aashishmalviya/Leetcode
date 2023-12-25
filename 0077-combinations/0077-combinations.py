class Solution:
    def __init__(self):
        self.temp_list = []
        self.result = []
        
    def combine(self, n: int, k: int) -> List[List[int]]:  
        temp_list = []
        result = []
        def combination_populator(start: int, n: int, k: int):
            nonlocal result, temp_list
            
            if len(temp_list) == k:
                result.append(temp_list[:])
                # print(self.result)
                return

            for i in range(start, n+1):
                temp_list.append(i)
                combination_populator(i+1, n, k)
                del temp_list[-1]

        combination_populator(1, n, k)
        return result