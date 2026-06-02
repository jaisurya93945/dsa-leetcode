# 🟢 LeetCode 128 - Longest Consecutive Sequence 😉

**Difficulty:** Medium
**Category:** Arrays & Hashing
**Author:** Jaisurya 😏

---

# 🎯 Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in:

```text
O(n)
```

---

## Example 1

```python
Input: nums = [100,4,200,1,3,2]

Output: 4
```

Explanation:

```text
1 → 2 → 3 → 4
```

Longest sequence length = **4**

---

## Example 2

```python
Input: nums = [0,3,7,2,5,8,4,6,0,1]

Output: 9
```

Explanation:

```text
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
```

Longest sequence length = **9**

---

# 🧠 Solution 1 — Brute Force

## Idea

For every number:

```python
100
4
200
1
3
2
```

Check:

```python
num + 1
num + 2
num + 3
...
```

until the sequence breaks.

---

## Visualization

Starting from:

```python
1
```

Check:

```python
2 ✓
3 ✓
4 ✓
5 ✗
```

Sequence length:

```python
4
```

---

## Code

```python
class Solution:

    def longestConsecutive(self, nums):

        longest = 0

        for num in nums:

            current = num
            streak = 1

            while current + 1 in nums:
                current += 1
                streak += 1

            longest = max(longest, streak)

        return longest
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| Time      | 🔴 O(n²)   |
| Space     | 🟢 O(1)    |

---

## Pros

✅ Easy to understand

## Cons

❌ Very slow

❌ Fails interview requirement

---

# 🧠 Solution 2 — Sorting

## Idea

Sort first.

Before:

```python
[100,4,200,1,3,2]
```

After:

```python
[1,2,3,4,100,200]
```

Now count consecutive numbers.

---

## Visualization

```text
1 → 2 → 3 → 4
```

Length:

```text
4
```

---

## Code

```python
class Solution:

    def longestConsecutive(self, nums):

        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                current += 1

            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
```

---

## Complexity

| Operation | Complexity    |
| --------- | ------------- |
| Time      | 🟡 O(n log n) |
| Space     | 🟢 O(1)       |

---

## Pros

✅ Easier than HashSet

✅ Good intermediate solution

## Cons

❌ Not O(n)

❌ Interviewers may ask for better

---

# 🚀 Solution 3 — HashSet (Optimal)

## Idea

Store all numbers inside a set.

```python
num_set = {100,4,200,1,3,2}
```

A number is a sequence starter only if:

```python
num - 1 NOT in set
```

---

## Example

For:

```python
1
```

```python
0 NOT in set
```

Therefore:

```python
1 starts a sequence
```

---

For:

```python
2
```

```python
1 exists
```

Therefore:

```python
2 does NOT start a sequence
```

---

## Visualization

```text
1 ✓ Start

2 ✗

3 ✗

4 ✗
```

Only one sequence scan happens.

---

## Code

```python
class Solution:

    def longestConsecutive(self, nums):

        num_set = set(nums)

        longest = 0

        for num in num_set:

            if num - 1 not in num_set:

                current = num
                streak = 1

                while current + 1 in num_set:

                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| Time      | 🟢 O(n)    |
| Space     | 🟡 O(n)    |

---

## Why O(n)?

Each number is visited at most once.

No repeated scanning.

---

## Pros

✅ Interview expected solution

✅ Fastest practical approach

✅ Elegant

---

## Cons

❌ Uses extra memory

---

# 🧠 Solution 4 — Union Find (Advanced)

## Idea

Treat numbers as connected components.

Example:

```text
1 -- 2 -- 3 -- 4
```

Component size:

```text
4
```

Use:

```python
Union Find
Disjoint Set Union (DSU)
```

---

## Code

```python
class DSU:

    def __init__(self):

        self.parent = {}
        self.size = {}

    def add(self, x):

        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]


class Solution:

    def longestConsecutive(self, nums):

        dsu = DSU()

        for num in nums:
            dsu.add(num)

        for num in nums:

            if num + 1 in dsu.parent:
                dsu.union(num, num + 1)

        answer = 0

        for root in dsu.parent:
            answer = max(
                answer,
                dsu.size[dsu.find(root)]
            )

        return answer
```

---

## Complexity

| Operation | Complexity   |
| --------- | ------------ |
| Time      | 🟢 O(n α(n)) |
| Space     | 🟡 O(n)      |

---

## Pros

✅ Advanced

✅ Great for system-level interviews

## Cons

❌ Overkill for this problem

❌ Harder to explain

---

# 📊 Comparison Table

| Solution    | Time       | Space | Interview Rating |
| ----------- | ---------- | ----- | ---------------- |
| Brute Force | O(n²)      | O(1)  | ⭐⭐               |
| Sorting     | O(n log n) | O(1)  | ⭐⭐⭐              |
| HashSet     | O(n)       | O(n)  | ⭐⭐⭐⭐⭐            |
| Union Find  | O(n α(n))  | O(n)  | ⭐⭐⭐⭐⭐⭐           |

---

# 🏆 Interview Winner

```text
HashSet Solution
```

Reason:

✅ O(n)

✅ Clean

✅ Easy to explain

✅ Most commonly expected answer

---

# 🎓 Key Learning

This problem teaches:

* HashSet
* Sequence detection
* Optimization
* Interview thinking
* Time complexity analysis

If you can derive the HashSet solution yourself, you're thinking like an interviewer wants.

---

# 🔥 Final Verdict

```text
Brute Force  → Learn
Sorting      → Understand
HashSet      → Master
Union Find   → Bonus Knowledge
```

---

## By Jaisurya 😉💚

*"Every optimized solution starts with a brute force idea."*
