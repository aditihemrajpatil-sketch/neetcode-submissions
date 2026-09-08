class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i =0
        n=len(arr)
        while 0<=i<n-1:
            rem_elements=arr[i+1:n]  
            arr[i]=max(rem_elements) 
            i+=1
        arr[-1] = -1 
        return arr
    