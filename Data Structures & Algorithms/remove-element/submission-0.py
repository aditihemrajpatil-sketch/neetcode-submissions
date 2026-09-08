class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k=n
        for i in range(n):
            if nums[i]==val:
                k-=1
        L,R=0,n-1
        while L < R and L < k:
            if nums[L]==val and nums[R]!=val:
                nums[L],nums[R]=nums[R],nums[L]
                L+=1
                R-=1
            elif nums[L]==val and nums[R]==val:
                R-=1
            elif nums[L]!=val and nums[R]==val:
                L+=1
                R-=1
            else:
                L+=1
        len(nums)==k
        return k


           



        