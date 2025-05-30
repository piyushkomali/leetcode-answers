class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        l, length = 0,0

        for r in range(len(s)):
            while s[r] in found:
                found.remove(s[l])
                l+=1
            found.add(s[r])
            length = max(length, r - l + 1)
        return length
