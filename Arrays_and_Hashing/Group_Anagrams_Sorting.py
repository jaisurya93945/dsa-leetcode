class Solution:
    def groupAnagrams(self, strs):

        # Dictionary to store grouped anagrams
        groups = {}

        # Loop through every word
        for word in strs:

            # Sort characters in word
            # Example:
            # "eat" -> "aet"
            sorted_word = "".join(sorted(word))

            # Check if sorted pattern already exists
            if sorted_word in groups:

                # Add word to existing group
                groups[sorted_word].append(word)

            else:
                # Create new group
                groups[sorted_word] = [word]

        # Return only grouped values
        return list(groups.values())
