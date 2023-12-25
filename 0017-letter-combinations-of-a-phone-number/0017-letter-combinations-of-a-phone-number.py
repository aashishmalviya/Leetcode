class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map ={'2' : 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9': 'xwyz'}

        result = []

        def combination_populator(current_combination, upcoming_digits):
            if len(upcoming_digits) == 0:
                result.append(current_combination)
                return

            front_digit = upcoming_digits[0]
            for letter in digit_map[front_digit]:
                combination_populator(current_combination + letter, upcoming_digits[1:])

        combination_populator("", digits)
        return result