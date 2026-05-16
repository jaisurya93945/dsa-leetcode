# 🚀 LeetCode Weekly Contest 501

> My first serious LeetCode Weekly Contest journey 🔥  
> Solved with Python 🐍

---

# 🏆 Problems Solved

| Problem | Difficulty | Status |
|---|---|---|
| Concatenate Array With Reverse | Easy 🟢 | ✅ Solved |
| Count Valid Word Occurrences | Medium 🟡 | ✅ Solved |

---

# 🧩 Problem 1 — Concatenate Array With Reverse

## 📄 Problem Statement

We are given an integer array called `nums`.

We need to create a NEW array where:

- first half = original array
- second half = reversed version of the same array

---

# 🧠 Example

## Input

```python
nums = [1,2,3]
```

## Output

```python
[1,2,3,3,2,1]
```

---

# 🐶 Simple Explanation (Golden Retriever Mode)

Imagine you have:

```python
[1,2,3]
```

Now:

1. Keep the original array
2. Flip it backwards
3. Attach it to the end

Like this:

```python
[1,2,3] + [3,2,1]
```

Final answer:

```python
[1,2,3,3,2,1]
```

---

# 💡 Main Concept Used

## Python Slicing

```python
nums[::-1]
```

This reverses the array.

---

# 🧠 Why?

Python slicing format:

```python
[start : end : step]
```

Using:

```python
[::-1]
```

means:
- start from end
- move backwards
- reverse everything

---

# ✅ Final Code

```python
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:

        ans = nums + nums[::-1]

        return ans
```

---

# ⏱️ Time Complexity

```text
O(n)
```

Because we traverse the array once.

---

# 📦 Space Complexity

```text
O(n)
```

Because we create a new array.

---

---

# 🧩 Problem 2 — Count Valid Word Occurrences

## 📄 Problem Statement

We are given:

- an array of string chunks
- an array of queries

First:
- combine all chunks into ONE string

Then:
- extract valid words carefully

Finally:
- count how many times each query appears as a FULL word

---

# 🧠 Example

## Input

```python
chunks = ["hello wor","ld hello"]
queries = ["hello","world","wor"]
```

After joining:

```python
"hello world hello"
```

Valid words:

```python
["hello", "world", "hello"]
```

Result:

```python
[2,1,0]
```

Because:
- `"hello"` appears 2 times
- `"world"` appears 1 time
- `"wor"` is NOT a full word

---

# ⚠️ Important Hyphen Rule

A hyphen `-` is valid ONLY IF:

```text
letter - letter
```

Example:

## ✅ Valid

```python
a-b
```

This becomes ONE word.

---

## ❌ Invalid

```python
a--b
```

This becomes:

```python
a
b
```

because double hyphen breaks the word.

---

# 🐶 Simple Explanation

Think of the program like reading a sentence letter by letter.

It builds words slowly:

```python
h → he → hel → hello
```

When:
- space appears
- invalid hyphen appears

the word ends and gets stored.

---

# 💡 Main Concepts Used

- String traversal
- Conditions
- Hashmaps / dictionaries
- Parsing
- Edge case handling

---

# ✅ Final Code

```python
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:

        # Join all chunks into one string
        s = "".join(chunks)

        # Store extracted words
        words = []

        # Current word being built
        current = ""

        # Traverse character by character
        for i in range(len(s)):

            ch = s[i]

            # Case 1: Letter
            if ch.isalpha():

                current += ch

            # Case 2: Hyphen
            elif ch == "-":

                # Valid joiner hyphen
                if (
                    i > 0
                    and i < len(s) - 1
                    and s[i - 1].islower()
                    and s[i + 1].islower()
                ):

                    current += ch

                # Invalid hyphen
                else:

                    if current:
                        words.append(current)

                    current = ""

            # Case 3: Separators / spaces
            else:

                if current:
                    words.append(current)

                current = ""

        # Add last word if remaining
        if current:
            words.append(current)

        # Count frequencies
        freq = {}

        for word in words:

            if word in freq:
                freq[word] += 1

            else:
                freq[word] = 1

        # Build final answer
        ans = []

        for q in queries:

            if q in freq:
                ans.append(freq[q])

            else:
                ans.append(0)

        return ans
```

---

# 🧠 Full Logic Breakdown

## Step 1 — Join All Strings

```python
s = "".join(chunks)
```

Example:

```python
["hello wor","ld hello"]
```

becomes:

```python
"hello world hello"
```

---

# Step 2 — Build Words

We scan every character.

If it is:
- letter → add to current word
- valid hyphen → add to current word
- separator → word ends

---

# Step 3 — Store Words

Example final words:

```python
["hello", "world", "hello"]
```

---

# Step 4 — Count Frequencies

Using hashmap:

```python
{
   "hello":2,
   "world":1
}
```

---

# Step 5 — Answer Queries

For every query:
- if exists → append count
- else → append 0

---

# ⏱️ Time Complexity

```text
O(n)
```

Where:
- `n` = total characters

---

# 📦 Space Complexity

```text
O(n)
```

Because:
- storing words
- storing hashmap

---

# 🏆 What I Learned From This Contest

✅ Arrays  
✅ Python slicing  
✅ Reversing arrays  
✅ String traversal  
✅ Hashmaps  
✅ Parsing  
✅ Debugging  
✅ Edge cases  
✅ Contest-style thinking  

---

# 🔥 Biggest Lesson

The hardest part is NOT syntax.

The hardest part is:
- understanding the problem
- breaking it into steps
- thinking logically

---

# 🚀 Contest Progress

| Problem | Result |
|---|---|
| Q1 | ✅ Solved |
| Q2 | ✅ Solved |
| Q3 | ⚡ Learned optimization & time complexity concepts |

---

# 🐍 Built With

- Python 3
- LeetCode
- Lots of debugging 😂

---

# ⭐ Final Note

This contest taught me:
> Good programmers don't just write code.  
> They understand the logic behind the code.
