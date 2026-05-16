# 🟢 Contains Duplicate — LeetCode

## 📌 Problem Statement

We are given an integer array called `nums`.

We need to return:

- `True` → if any number appears more than once
- `False` → if all numbers are unique

---

# 🧠 Example

## Input
```python
nums = [1,2,3,1]
```

## Output
```python
True
```

👉 Because number `1` appears two times.

---

# 🥊 Solution 1 — Brute Force Approach

## 💡 Idea

We compare every number with every other number.

If we find two same numbers at different positions:
👉 return `True`

Otherwise:
👉 return `False`

---

# 👶 Child Explanation

Imagine you have a basket of balls 🎾

You pick one ball and compare it with every other ball.

If you find another ball with the same number:
👉 "Duplicate found!"

If not:
👉 keep checking.

---

# 🧾 Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] == nums[j]:
                    return True

        return False
```

---

# ⏱ Time Complexity

```text
O(n²)
```

Because we are using two loops.

---

# 📦 Space Complexity

```text
O(1)
```

No extra space used.

---

---

# ⚡ Solution 2 — Using set()

## 💡 Idea

A `set()` stores only unique values.

So:
- if number already exists in set
👉 duplicate found

Otherwise:
👉 add number into set

---

# 👶 Child Explanation

Imagine a magic bag 🎒

The bag only allows one copy of each number.

If you try putting same number again:
👉 bag says:
```text
"HEY! I already have this!"
```

That means duplicate found 😄

---

# 🧾 Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        storage = set()

        for num in nums:

            if num in storage:
                return True

            storage.add(num)

        return False
```

---

# ⏱ Time Complexity

```text
O(n)
```

Because we check each element only once.

---

# 📦 Space Complexity

```text
O(n)
```

Because set stores elements.

---

# 🏆 Best Solution

✅ `set()` solution is better because:

- Faster
- Cleaner
- More optimized

---

# 🎯 What I Learned

✅ Brute force checking  
✅ Nested loops  
✅ How set() works  
✅ Faster duplicate detection  
✅ Time complexity basics

---

# 🚀 GitHub Progress

- ✅ Solved Contains Duplicate
- ✅ Learned brute force
- ✅ Learned optimized set() approach
- ✅ Uploaded explanation and code
