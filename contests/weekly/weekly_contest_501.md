# Weekly Contest 501

# Problem 1 — Concatenate Array With Reverse

## Difficulty
Easy

---

# Problem Statement

We are given an array called `nums`.

We need to create a NEW array where:

- first half = original array
- second half = reversed array

---

# Example

## Input

```python
nums = [1,2,3]
```

## Output

```python
[1,2,3,3,2,1]
```

---

# My Understanding

The problem is NOT asking to only reverse the array.

Instead:

1. Keep the original array
2. Reverse the same array
3. Attach the reversed array to the original one
4. Return the final combined array

So basically:

```python
original array + reversed array
```

---

# Step-by-Step Thinking

Suppose:

```python
nums = [1,2,3]
```

---

## Step 1 — Original Array

```python
[1,2,3]
```

---

## Step 2 — Reverse the Array

Using:

```python
nums[::-1]
```

We get:

```python
[3,2,1]
```

---

## Step 3 — Combine Both Arrays

```python
[1,2,3] + [3,2,1]
```

Final Answer:

```python
[1,2,3,3,2,1]
```

---

# Full Code

```python
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:

        ans = nums + nums[::-1]

        return ans
```

---

# Full Code Explanation

## Line 1

```python
class Solution:
```

LeetCode already expects our solution inside a class called `Solution`.

---

## Line 2

```python
def concatWithReverse(self, nums: list[int]) -> list[int]:
```

This creates the function.

### Parameters

```python
nums
```

The input array.

---

## Return Type

```python
-> list[int]
```

Means the function returns a list of integers.

---

# Main Logic

## This Line

```python
ans = nums + nums[::-1]
```

This is the most important line.

---

# First Part

```python
nums
```

Gives the original array.

Example:

```python
[1,2,3]
```

---

# Second Part

```python
nums[::-1]
```

Reverses the array.

Example:

```python
[3,2,1]
```

---

# Then `+`

The `+` operator combines both arrays.

So:

```python
[1,2,3] + [3,2,1]
```

Becomes:

```python
[1,2,3,3,2,1]
```

---

# Final Return

```python
return ans
```

Returns the final array.

---

# Understanding `nums[::-1]`

Python slicing format:

```python
[start : end : step]
```

Here:

```python
[::-1]
```

Means:
- start from end
- move backwards
- step = `-1`

That is why the array gets reversed.

---

# Time Complexity

```text
O(n)
```

Because:
- Python traverses the array once to reverse it.

---

# Space Complexity

```text
O(n)
```

Because:
- we create a new array.

---

# What I Learned

- Array concatenation
- Python slicing
- Reversing arrays
- Creating new arrays
- Returning transformed arrays
- Breaking problems into smaller logical steps

---

# Contest Notes

This was my first LeetCode Weekly Contest problem.

Main lesson:
- Understand the problem first
- Break it into steps
- Then write the cleanest possible solution
