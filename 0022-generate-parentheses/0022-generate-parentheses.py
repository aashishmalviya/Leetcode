class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def generator(current_string, open_count, close_count):

            if close_count == n:
                result.append(current_string)
                return

            if open_count < n:
                generator(current_string + '(', open_count+1, close_count)

            if close_count < open_count:
                generator(current_string + ')', open_count, close_count+1)

        generator("", 0, 0)
        return result