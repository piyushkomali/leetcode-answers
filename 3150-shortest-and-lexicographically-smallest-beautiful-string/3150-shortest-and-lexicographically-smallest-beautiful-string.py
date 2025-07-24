class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ret = ''
        i,j=0,0
        countK=0
        while j<n:
            if s[j] == '1':
                countK+=1
            if countK == k:
                while i < n and countK == k:
                    newS = s[i:j+1]
                    if not ret or len(newS) < len(ret):
                        ret = newS
                    if len(newS) == len(ret):
                        ret = min(newS, ret)
                    if s[i] == '1': countK-=1
                    i+=1
            j+=1
        return ret

        