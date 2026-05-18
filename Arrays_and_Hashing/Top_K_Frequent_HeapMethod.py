import heapq

class Solution:
    def topKFrequent(self, nums, k):

        # Frequency dictionary
        freq = {}

        # Count frequency
        for num in nums:

            freq[num] = freq.get(num, 0) + 1

        # Create heap
        heap = []

        # Push frequency and number
        for num, count in freq.items():

            heapq.heappush(heap, (-count, num))

        # Final result
        result = []

        # Extract top k elements
        for _ in range(k):

            count, num = heapq.heappop(heap)

            result.append(num)

        return result
