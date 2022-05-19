class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            value = -1*int(''.join(list(str(x))[::-1]))
            if value <= -2**31:
                return 0
            return value
        value = int(''.join(list(str(x))[::-1]))
        if value >= (2**31) - 1:
            return 0
        return value


reverse = Solution()
answer = reverse.reverse(123)

print(answer)
# print()
# print(-8463847412)