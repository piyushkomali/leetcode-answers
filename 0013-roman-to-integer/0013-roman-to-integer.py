class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        length = len(arr) -1
        count = 0
        i = 0
        rmap = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        while (i < length+1):
            currVal = rmap[arr[i]]
            if (i != length and rmap[arr[i+1]] > currVal):
                count += rmap[arr[i+1]] - currVal
                i += 1
            else:
                count += currVal
            i += 1
        return count


