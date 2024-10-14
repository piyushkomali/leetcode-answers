class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefixLen = len(prefix)

        for s in strs[1:]:
            while prefix != s[:prefixLen]:
                prefixLen -=1
                if (prefixLen == 0):
                    return ""
                prefix = prefix[0:prefixLen]
        return prefix



