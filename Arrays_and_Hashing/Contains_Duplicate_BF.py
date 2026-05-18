class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j and nums[i] == nums[j]:
                    return True
        return False
