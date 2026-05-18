class Solution:
    def groupAnagrams(self, strs):

        # Dictionary to store grouped anagrams
        groups = {}

        # Loop through every word
        for word in strs:

            # Create frequency array for 26 letters
            # Initially all counts are 0
            count = [0] * 26

            # Count every character
            for char in word:

                # Convert character into index
                # ord('a') = 97
                # ord(char) - ord('a')
                # gives position from 0-25
                index = ord(char) - ord('a')

                # Increase character count
                count[index] += 1

            # Convert list to tuple
            # Because lists cannot be dictionary keys
            key = tuple(count)

            # Check if key exists
            if key in groups:

                # Add word to existing group
                groups[key].append(word)

            else:
                # Create new group
                groups[key] = [word]

        # Return grouped anagrams
        return list(groups.values())
