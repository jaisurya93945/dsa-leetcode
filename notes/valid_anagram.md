# 🟢 Valid Anagram — LeetCode

## 📌 Problem Statement

We are given two strings:

```python
s
t
```

We need to return:

- `True` → if both strings are anagrams
- `False` → otherwise

---

# 🧠 What is an Anagram?

Two strings are called anagrams if:

✅ They contain the SAME letters  
✅ The letters appear SAME number of times

Order does NOT matter.

---

# 🧠 Example

## Input

```python
s = "listen"
t = "silent"
```

## Output

```python
True
```

Because both strings contain:

```text
l, i, s, t, e, n
```

same letters with same counts.

---

# ❌ Not Anagram Example

## Input

```python
s = "rat"
t = "car"
```

## Output

```python
False
```

Different letters.

---

---

# 🥊 Solution 1 — Using Two Dictionaries

## 💡 Idea

We count how many times each letter appears in BOTH strings.

Then compare both dictionaries.

If equal:
✅ anagram

Else:
❌ not anagram

---

# 👶 Child Explanation

Imagine two toy boxes 📦

We count toys inside each box.

If both boxes contain same toys same number of times:
✅ they match

Otherwise:
❌ they don't match

---

# 🧾 Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Lengths must be same
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        # Count letters in first string
        for ch in s:

            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1

        # Count letters in second string
        for ch in t:

            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1

        # Compare both dictionaries
        return dict1 == dict2
```

---

# ⏱ Time Complexity

```text
O(n)
```

---

# 📦 Space Complexity

```text
O(n)
```

Because dictionaries store characters.

---

---

# ⚡ Solution 2 — Using One Dictionary

## 💡 Idea

Instead of two dictionaries:

- First string ➜ increase count 📈
- Second string ➜ decrease count 📉

At the end:
if all values become `0`
✅ valid anagram

---

# 👶 Child Explanation

Imagine a score board 🎯

First string ADDS points.

Second string REMOVES points.

If everything becomes `0`
👉 perfect match!

---

# 🧾 Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Lengths must be same
        if len(s) != len(t):
            return False

        count = {}

        # Add letters from first string
        for ch in s:

            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Remove letters using second string
        for ch in t:

            if ch in count:
                count[ch] -= 1
            else:
                return False

        # Check all values
        for value in count.values():

            if value != 0:
                return False

        return True
```

---

# ⏱ Time Complexity

```text
O(n)
```

---

# 📦 Space Complexity

```text
O(n)
```

---

# 🏆 Which Solution is Better?

| Solution | Best For |
|---|---|
| Two Dictionaries | Beginners & learning |
| One Dictionary | Cleaner & interviews |

---

# 🎯 What I Learned

✅ Hashmaps / Dictionaries  
✅ Frequency counting  
✅ String traversal  
✅ Optimized counting logic  
✅ Anagram pattern recognition

---

# 🚀 GitHub Progress

- ✅ Solved Valid Anagram
- ✅ Learned dictionary counting
- ✅ Learned optimized hashmap approach
- ✅ Improved DSA pattern understanding
