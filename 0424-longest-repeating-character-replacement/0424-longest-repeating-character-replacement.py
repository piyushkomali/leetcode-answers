class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap_for_window = {}
        maxLen = 0
        currentWindowsMaxCount = 0
        l=0
        for r in range(len(s)):
            #in the cur window this is count for all the distinct chars e2: AAABA{A:3,B:1}
            countMap_for_window[s[r]] = countMap_for_window.get(s[r],0)+1
            #this is the maxCount of any character in the window(A:3)
            currentWindowsMaxCount = max(currentWindowsMaxCount,countMap_for_window[s[r]])

            windowSize = r-l+1
            #AAABA (ws:5, maxCo: 4 - VALID) | AAABAB (ws:6, maxCo: 4 - INVALID)
            # So 
            if(windowSize - currentWindowsMaxCount > k):
                countMap_for_window[s[l]]-=1
                currentWindowsMaxCount-=1
                l+=1
            #it will get here if window is valid with an acceptable no. of replacements
            #can use windowSz, bc if we move LP windowsz isnt valid anymore
            maxLen = max(maxLen, r-l+1)
        return maxLen
        