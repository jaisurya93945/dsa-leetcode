class Solution:
    def groupAnagrams(self, strs):

        # Prime numbers for each alphabet
        primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7,
            'e': 11, 'f': 13, 'g': 17, 'h': 19,
            'i': 23, 'j': 29, 'k': 31, 'l': 37,
            'm': 41, 'n': 43, 'o': 47, 'p': 53,
            'q': 59, 'r': 61, 's': 67, 't': 71,
            'u': 73, 'v': 79, 'w': 83, 'x': 89,
            'y': 97, 'z': 101
        }

        # Dictionary to store groups
        groups = {}

        # Loop through words
        for word in strs:

            # Start multiplication value
            product = 1

            # Multiply prime values
            for char in word:

                product *= primes[char]

            # Same product = same anagram

            if product in groups:
                groups[product].append(word)
            else:
                groups[product] = [word]

        return list(groups.values())
