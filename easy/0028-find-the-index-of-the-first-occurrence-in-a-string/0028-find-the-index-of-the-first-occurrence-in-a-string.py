class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        h = list(haystack)
        n = list(needle)
        for i in range(len(h) - len(n) +1):
            if h[i] == n[0]:
                ans = i

                for x in range(1,len(n)):
                    if h[i+x] != n[x]:
                        ans = -1
                if(ans!=-1):
                    break
                
        return ans
        