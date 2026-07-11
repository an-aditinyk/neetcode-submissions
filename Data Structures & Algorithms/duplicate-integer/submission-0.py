class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=0
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if (nums[i]==nums[j]):
                    a=1
                    return True
            
        if (a!=1):
            return False        
