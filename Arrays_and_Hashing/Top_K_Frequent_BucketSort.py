class Solution:
    def topKFrequent(self, nums, k):

        # Count frequency
        freq = {}

        for num in nums:

            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        # Index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]

        # Place numbers into bucket
        for num, count in freq.items():

            bucket[count].append(num)

        # Final result
        result = []

        # Traverse buckets backwards
        for i in range(len(bucket) - 1, 0, -1):

            for num in bucket[i]:

                result.append(num)

                # Stop once k elements found
                if len(result) == k:
                    return result
