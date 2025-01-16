class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        r = [0] * length
        m = arr[length-1]
        for i in range(length-1,-1,-1):
            if i==length-1:
                r[i] = -1
            else:
                r[i]=m
                m = max(m,arr[i])
        return r
                

        