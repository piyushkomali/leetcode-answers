class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        r = [0] * length
        m = arr[length-1]
        for i in range(length-2,-1,-1):
            r[i]=m
            m = max(m,arr[i])
        r[length-1]=-1
        return r
                

        