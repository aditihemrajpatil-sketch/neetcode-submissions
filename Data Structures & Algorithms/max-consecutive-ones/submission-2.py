class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        lists=[]
        for i in range(len(nums)):
            if nums[i]==1 :
                count+=1
            
            elif nums[i]==0 and nums[i-1]==1:
                lists.append(count)
                count=0
            else :
                continue
        lists.append(count)
        return max(lists)