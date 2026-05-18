# 🎯 Weekly Contest 502 — Full Detailed Notes
## 🚀 AI Security Engineer DSA Journey

---

# 📌 Q1. Check Adjacent Digit Differences

## 🟢 Difficulty
Easy

## 🧠 Topics
- String
- Traversal
- Math

---

# 📖 Problem Statement

You are given a string `s` consisting of digits.

Return `true` if the absolute difference between every pair of adjacent digits is at most `2`, otherwise return `false`.

---

## ✅ Example 1

```python
Input: s = "132"

Output: true
```

### Explanation

```python
abs(1 - 3) = 2
abs(3 - 2) = 1
```

Both are ≤ 2

So answer is:

```python
True
```

---

## ❌ Example 2

```python
Input: s = "129"

Output: false
```

### Explanation

```python
abs(1 - 2) = 1
abs(2 - 9) = 7
```

7 > 2

So answer is:

```python
False
```

---

# 🧠 Core Idea

We compare every digit with its next adjacent digit.

If ANY difference becomes greater than `2`:

```python
return False
```

Otherwise:

```python
return True
```

---

# ✅ Accepted Code

```python
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:

        # Traverse all adjacent pairs
        for i in range(len(s) - 1):

            # Convert string digits into integers
            a = int(s[i])
            b = int(s[i + 1])

            # Check absolute difference
            if abs(a - b) > 2:
                return False

        return True
```

---

# 🔍 Line-by-Line Explanation

---

## 🔹 Loop Through Adjacent Digits

```python
for i in range(len(s) - 1):
```

If:

```python
s = "132"
```

Indexes:

```python
0 1 2
```

Comparisons:

```python
1 with 3
3 with 2
```

---

## 🔹 Convert Character into Integer

```python
a = int(s[i])
b = int(s[i + 1])
```

Because:

```python
"1"
```

is a string.

Need integer:

```python
1
```

---

## 🔹 Absolute Difference

```python
abs(a - b)
```

Examples:

```python
abs(1 - 3) = 2
abs(5 - 2) = 3
```

Absolute means positive distance.

---

## 🔹 Condition Check

```python
if abs(a - b) > 2:
```

If difference becomes greater than 2:

```python
return False
```

---

## 🔹 Final Return

```python
return True
```

Means every adjacent pair was valid.

---

# ⏱️ Complexity

## Time Complexity

```python
O(n)
```

---

## Space Complexity

```python
O(1)
```

---

---

# 📌 Q2. Count K-th Roots in a Range

## 🟡 Difficulty
Medium

## 🧠 Topics
- Math
- Binary Search
- Powers

---

# 📖 Problem Statement

You are given:

```python
l, r, k
```

An integer `y` is called a perfect kth power if:

```python
y = x^k
```

for some integer `x`.

Return the number of perfect kth powers in range:

```python
[l, r]
```

---

# ✅ Example 1

```python
Input: l = 1, r = 9, k = 3

Output: 2
```

---

## 🔍 Explanation

Perfect cubes:

```python
1 = 1^3
8 = 2^3
```

Answer:

```python
2
```

---

# ✅ Example 2

```python
Input: l = 8, r = 30, k = 2

Output: 3
```

---

## 🔍 Explanation

Perfect squares:

```python
9  = 3^2
16 = 4^2
25 = 5^2
```

Answer:

```python
3
```

---

# 🧠 Core Idea

Instead of checking every number:

We count how many integers satisfy:

```python
x^k <= r
```

Then subtract:

```python
x^k < l
```

---

# ⚡ Binary Search Insight

Powers increase monotonically:

```python
1^k < 2^k < 3^k < 4^k
```

So binary search works perfectly.

---

# ✅ Accepted Code

```python
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        # Helper function
        # Counts numbers where x^k <= n
        def count(n):

            if n < 0:
                return 0

            left = 0
            right = 10**9

            while left <= right:

                mid = (left + right) // 2

                power = mid ** k

                if power <= n:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        return count(r) - count(l - 1)
```

---

# 🔍 Detailed Explanation

---

## 🔹 Binary Search Range

```python
left = 0
right = 10**9
```

Maximum possible root.

---

## 🔹 Middle Element

```python
mid = (left + right) // 2
```

Standard binary search midpoint.

---

## 🔹 Compute Power

```python
power = mid ** k
```

Example:

```python
mid = 3
k = 2

3^2 = 9
```

---

## 🔹 Valid Root

```python
if power <= n:
```

Means:

```python
mid
```

is valid.

Move right.

---

## 🔹 Too Large

```python
else:
```

Power exceeded limit.

Move left.

---

# ⏱️ Complexity

## Time Complexity

```python
O(log n)
```

---

## Space Complexity

```python
O(1)
```

---

---

# 📌 Q3. Largest Local Values in a Matrix II

## 🟡 Difficulty
Medium

## 🧠 Topics
- Matrix
- Simulation
- Optimization
- Traversal

---

# 📖 Problem Statement

For every non-zero cell:

```python
matrix[row][col]
```

Let:

```python
x = matrix[row][col]
```

Check nearby cells:
- within `x` rows
- within `x` columns

Ignore:
- cells outside matrix
- corner cells where BOTH row and column distance equal `x`

A cell is local maximum if:
NO checked cell has value GREATER than it.

---

# ✅ Example

```python
matrix =
[
 [1,0,1],
 [0,1,0],
 [1,0,1]
]
```

Answer:

```python
5
```

---

# 🔍 Explanation

Each `1` only sees:
- itself
- nearby 0s
- nearby 1s

No larger values exist.

So all five cells are local maximums.

---

# ❌ Initial Problem

Brute force solution caused:

```python
TLE = Time Limit Exceeded
```

because matrix traversal became huge.

---

# 🧠 Important Optimization

Use:
- bounded traversal
- early stopping

---

# ✅ Final Accepted Code

```python
class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        ans = 0

        # Traverse every cell
        for row in range(n):
            for col in range(m):

                x = matrix[row][col]

                # Ignore zero cells
                if x == 0:
                    continue

                is_local = True

                # Traverse nearby area
                for r in range(max(0, row - x), min(n, row + x + 1)):

                    # Early stopping
                    if not is_local:
                        break

                    for c in range(max(0, col - x), min(m, col + x + 1)):

                        dr = abs(r - row)
                        dc = abs(c - col)

                        # Ignore corner cells
                        if dr == x and dc == x:
                            continue

                        # Found larger value
                        if matrix[r][c] > x:
                            is_local = False
                            break

                # Valid local maximum
                if is_local:
                    ans += 1

        return ans
```

---

# 🔍 Detailed Explanation

---

## 🔹 Matrix Dimensions

```python
n = len(matrix)
m = len(matrix[0])
```

Rows and columns.

---

## 🔹 Traverse Every Cell

```python
for row in range(n):
    for col in range(m):
```

Standard matrix traversal.

---

## 🔹 Ignore Zero Cells

```python
if x == 0:
    continue
```

Only non-zero cells matter.

---

## 🔹 Nearby Traversal

```python
for r in range(max(0, row - x), min(n, row + x + 1)):
```

Avoid going outside matrix.

---

## 🔹 Ignore Corners

```python
if dr == x and dc == x:
    continue
```

Exactly matches problem statement.

---

## 🔹 Greater Value Found

```python
if matrix[r][c] > x:
```

Cell fails local maximum condition.

---

## 🔹 Early Exit Optimization

```python
if not is_local:
    break
```

Huge runtime optimization.

---

# 🧠 Contest Lessons Learned

---

## ✅ Correct Logic ≠ Accepted

Even correct solutions can fail runtime.

---

## ✅ Hidden Testcases Matter

Worst-case performance matters.

---

## ✅ Optimization Is Real Engineering

This directly relates to:
- malware scanning
- AI tensor operations
- GPU workloads
- memory optimization
- cybersecurity tools

---

# 🚀 AI Security Engineer Relevance

These DSA concepts help in:

- Threat detection systems
- Malware scanners
- Efficient AI inference
- Memory optimization
- Large-scale data traversal
- Tensor reasoning
- GPU pipeline understanding

---

# 🏆 Topics Learned Overall

| Problem | Topics |
|---|---|
| Q1 | Strings, Traversal |
| Q2 | Binary Search, Math |
| Q3 | Matrix, Optimization |

---

# 🧠 Final Takeaway

DSA is NOT just interview prep.

It trains:
- problem solving
- optimization thinking
- runtime analysis
- engineering mindset

These are core skills for becoming:
# 🔥 AI Security Engineer
