class Solution:
    def topKFrequent(self, nums, k):

        # Final result
        result = []

        # Keep track of used numbers
        used = set()

        # Repeat k times
        for _ in range(k):

            max_count = 0
            max_num = None

            # Check every number
            for num in nums:

                # Skip already selected numbers
                if num in used:
                    continue

                # Count frequency manually
                count = nums.count(num)

                # Find maximum frequency
                if count > max_count:
                    max_count = count
                    max_num = num

            # Add best number
            result.append(max_num)

            # Mark as used
            used.add(max_num)

        return result
