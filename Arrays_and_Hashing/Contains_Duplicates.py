class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()

        for i in range(len(nums)):
            number = nums[i]

            if number in storage:
                return True
            storage.add(number)
        return False
