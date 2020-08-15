class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)

        if output >= 2 ** 31 - 1 or output <= -2 ** 31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output


sol = Solution()
print(sol.reverse(-123))