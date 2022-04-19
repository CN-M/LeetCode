class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

answer = Solution()

print(answer.isPalindrome(121))