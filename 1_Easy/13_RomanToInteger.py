class Solution:
    def romanToInt(self, s: str) -> int:
        listed = list(s.upper())
        
        for i,n in enumerate(listed):
            if n == 'I':
                listed[i] = 1
            if n == 'V':
                listed[i] = 5
            if n == 'X':
                listed[i] = 10
            if n == 'L':
                listed[i] = 50
            if n == 'C':
                listed[i] = 100
            if n == 'D':
                listed[i] = 500
            if n == 'M':
                listed[i] = 1000

        for i,n in enumerate(listed):
            try:
                if listed[i] < listed[i+1]:
                    listed[i] = n*(-1)
            except:
                pass
        
        return sum(listed)

class Solution2:
    def romanToInt(self, s: str) -> int:
        listed = list(s)
        ref = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i,n in enumerate(listed):
            listed[i] = ref[n]
        for i,n in enumerate(listed):
            try:
                if listed[i] < listed[i+1]:
                    listed[i] = n*(-1)
            except:
                pass
        return sum(listed)


answer = Solution2()

print(answer.romanToInt("MCMXCIV"))