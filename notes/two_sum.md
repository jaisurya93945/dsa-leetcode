# Two Sum

For this problem, I implemented two different solutions:

1. Brute Force Solution
2. Optimized HashMap Solution

---

# 1. Brute Force Solution

## Idea
The brute force approach checks every possible pair in the array.

## Logic
- Use the first loop to pick one element.
- Use the second loop to compare it with remaining elements.
- Use `i + 1` to avoid comparing the same element again.
- If the sum equals the target, return the indices.

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]
