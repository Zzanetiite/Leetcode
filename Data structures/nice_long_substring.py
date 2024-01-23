from typing import List


class Solution:

    def longestNiceSubstringRecursive(self, s: str) -> str:
        if len(s) < 2:
            return ""
        for i in range(len(s)):
            if s[i].swapcase() not in s:
                s1 = self.longestNiceSubstringRecursive(s[0:i])
                s2 = self.longestNiceSubstringRecursive(s[i+1:len(s)])
                return max(s1, s2, key=len)
        return s


result = Solution().longestNiceSubstringRecursive(
    "YazaAayasdawassfsafaaaaAbbbBcdccCD")
print("Result: ", result)
