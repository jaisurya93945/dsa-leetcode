class Solution:
    def groupAnagrams(self, strs):

        # Final result list
        result = []

        # Keep track of words already grouped
        visited = set()

        # Loop through every word
        for i in range(len(strs)):

            # Skip if already grouped
            if strs[i] in visited:
                continue

            # Start a new group with current word
            group = [strs[i]]

            # Mark current word as visited
            visited.add(strs[i])

            # Compare with remaining words
            for j in range(i + 1, len(strs)):

                # Check if both words are anagrams
                if sorted(strs[i]) == sorted(strs[j]):

                    # Add matching anagram
                    group.append(strs[j])

                    # Mark as visited
                    visited.add(strs[j])

            # Add completed group to result
            result.append(group)

        return result
