class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        storage = {}

        for i in range(len(nums)):

            thing = target - nums[i]

            if thing in storage:
                return [storage[thing], i]
            storage[nums[i]] = i
