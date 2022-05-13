class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = []
        compare = {}
        for i,n in enumerate(list(s)):
            if n in hash:
                compare[i] = ''.join(hash[:i])
                hash = []
            hash.append(n)
        
        listOflengths = [len(compare[i]) for i in compare]
        if not listOflengths and len(s) < 1:
            if ' ' in s or '' in s :
                return s.count(' ')
        return max(listOflengths)

answer = Solution()
sol = answer.lengthOfLongestSubstring("abcabcbb")
# sol = answer.lengthOfLongestSubstring('pwwkew')
# sol = answer.lengthOfLongestSubstring(' ')

print(sol)

