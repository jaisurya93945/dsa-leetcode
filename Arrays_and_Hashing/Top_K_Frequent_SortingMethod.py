class Solution:
    def topKFrequent(self, nums, k):

        # Frequency dictionary
        freq = {}

        # Count frequency
        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Convert into list
        freq_list = list(freq.items())

        # Sort using frequency
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # Store answer
        result = []

        # Take first k elements
        for i in range(k):

            result.append(freq_list[i][0])

        return result
