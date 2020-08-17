class Solution:
    SPACE_CHARACTERS = " "
    SIGNAL_CHARACTERS = "+-"
    DIGIT_CHARACTERS = "0123456789"
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    @staticmethod
    def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """

        sign = None
        spaces_ended = False
        digits = []

        for char in str:
            if char in Solution.SPACE_CHARACTERS and not spaces_ended:
                continue
            else:
                spaces_ended = True
            if char in Solution.SIGNAL_CHARACTERS and not sign:
                sign = 1 if char == "+" else -1

            elif char in Solution.DIGIT_CHARACTERS:
                sign = 1 if not sign else sign
                digits.append(char)
            else:
                break

        total = 0
        sign = 1 if not sign else sign

        for i in range(0, len(digits)):
            total += Solution.DIGIT_CHARACTERS.index(digits[i]) * 10 ** (len(digits) - i - 1)
        total *= sign

        if total < Solution.INT_MIN:
            return Solution.INT_MIN
        elif total > Solution.INT_MAX:
            return Solution.INT_MAX
        else:
            return total