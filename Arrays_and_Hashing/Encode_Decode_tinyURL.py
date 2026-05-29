from collections import defaultdict

class Codec:
    def __init__(self):
        # Dictionary to store mapping from short URL ID to long URL
        self.url_map = defaultdict(str)
        # Counter for generating unique IDs for each URL
        self.counter = 0
        # Base domain for the shortened URLs
        self.base_domain = 'https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
      
        Args:
            longUrl: The original long URL to be shortened
          
        Returns:
            A shortened URL with format: https://tinyurl.com/{id}
        """
        # Increment counter to generate a unique ID
        self.counter += 1
        # Store the mapping from ID to long URL
        self.url_map[str(self.counter)] = longUrl
        # Return the shortened URL
        return f'{self.base_domain}{self.counter}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
      
        Args:
            shortUrl: The shortened URL to be decoded
          
        Returns:
            The original long URL
        """
        # Extract the ID from the shortened URL (last part after)
        url_id = shortUrl.split('/')[-1]
        # Look up and return the original URL using the ID
        return self.url_map[url_id]
