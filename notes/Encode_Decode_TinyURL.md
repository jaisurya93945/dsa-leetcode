# 🔗 LeetCode 535 - Encode and Decode TinyURL

## Difficulty

🟢 Medium

## Topic

* Hash Map
* String Manipulation
* Design

---

# Problem Statement

Design a URL shortening service similar to TinyURL.

Implement the `Codec` class:

```python
class Codec:

    def encode(self, longUrl: str) -> str:
        pass

    def decode(self, shortUrl: str) -> str:
        pass
```

### Example

```python
Input:
https://leetcode.com/problems/design-tinyurl

Output:
https://tinyurl.com/1
```

---

# Approach 1: Counter Based Mapping

## Intuition

Instead of generating random strings, assign each URL a unique integer ID.

Example:

```text
1 -> https://google.com
2 -> https://github.com
3 -> https://leetcode.com
```

When encoding:

1. Increment counter
2. Store URL in dictionary
3. Return tiny URL

When decoding:

1. Extract ID from short URL
2. Lookup original URL in dictionary
3. Return original URL

---

# Data Structures Used

```python
url_map = {
    "1": "https://google.com",
    "2": "https://github.com"
}
```

---

# Code

```python
from collections import defaultdict

class Codec:

    def __init__(self):

        self.url_map = defaultdict(str)

        self.counter = 0

        self.base_domain = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:

        self.counter += 1

        self.url_map[str(self.counter)] = longUrl

        return f"{self.base_domain}{self.counter}"

    def decode(self, shortUrl: str) -> str:

        url_id = shortUrl.split("/")[-1]

        return self.url_map[url_id]
```

---

# Dry Run

## Encode

Input:

```python
https://google.com
```

Counter:

```python
1
```

Dictionary:

```python
{
    "1": "https://google.com"
}
```

Output:

```python
https://tinyurl.com/1
```

---

## Decode

Input:

```python
https://tinyurl.com/1
```

Extract ID:

```python
1
```

Lookup:

```python
url_map["1"]
```

Output:

```python
https://google.com
```

---

# Complexity Analysis

## Encode

```text
Time Complexity: O(1)
```

Only:

* Increment counter
* Dictionary insertion

---

## Decode

```text
Time Complexity: O(1)
```

Only:

* Extract ID
* Dictionary lookup

---

## Space Complexity

```text
O(n)
```

Where:

```text
n = number of URLs stored
```

---

# Advantages

✅ Very easy to implement

✅ O(1) encode

✅ O(1) decode

✅ No collisions

✅ Great interview starter solution

---

# Disadvantages

❌ URLs are predictable

```text
tinyurl.com/1
tinyurl.com/2
tinyurl.com/3
```

❌ Not suitable for production

❌ Users can guess other URLs

---

# Interview Follow-Up

### How would you improve this?

Use:

```python
Random Hashing
```

Generate:

```text
aBc123
XyZ789
QWE456
```

instead of:

```text
1
2
3
```

This prevents URL enumeration attacks and looks more like a real TinyURL service.

---

# Key Takeaway

This solution demonstrates:

* Hash Map usage
* Design thinking
* URL mapping
* Constant time lookups

It is the simplest and cleanest solution for understanding the TinyURL problem before moving to Random Hashing or Base62 Encoding.
