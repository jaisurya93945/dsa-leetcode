# 🔥 Product of Array Except Self — COMPLETE GUIDE
## LeetCode 238

---

# 📌 Difficulty
Medium

# 📌 Main Topic
- Arrays

# 📌 Secondary Topics
- Prefix Products
- Suffix Products
- Space Optimization

---

# 📖 Problem Statement

Given an integer array:

```python
nums
```

Return an array:

```python
answer
```

where:

```python
answer[i]
```

is equal to the product of ALL elements of `nums`
EXCEPT:

```python
nums[i]
```

---

# ⚠️ Rules

- ❌ Do NOT use division
- ✅ Time Complexity should be:

```python
O(n)
```

---

# ✅ Example

Input:

```python
nums = [1,2,3,4]
```

Output:

```python
[24,12,8,6]
```

---

# 🔍 Explanation

For index 0:

```python
2 * 3 * 4 = 24
```

For index 1:

```python
1 * 3 * 4 = 12
```

For index 2:

```python
1 * 2 * 4 = 8
```

For index 3:

```python
1 * 2 * 3 = 6
```

Final Answer:

```python
[24,12,8,6]
```

---

# 🧠 METHOD 1 — BRUTE FORCE

## 🔥 Idea

For every element:
- multiply ALL remaining elements
- skip current element

---

# ✅ Brute Force Code

```python
class Solution:
    def productExceptSelf(self, nums):

        # Final answer list
        result = []

        # Loop through every index
        for i in range(len(nums)):

            # Start product as 1
            product = 1

            # Multiply all elements except current index
            for j in range(len(nums)):

                # Skip same index
                if i != j:

                    product *= nums[j]

            # Store result
            result.append(product)

        return result
```

---

# 🔍 Detailed Explanation

---

## 🔹 Outer Loop

```python
for i in range(len(nums)):
```

This selects current element.

---

## 🔹 Product Variable

```python
product = 1
```

Starts multiplication.

---

## 🔹 Inner Loop

```python
for j in range(len(nums)):
```

Traverse entire array again.

---

## 🔹 Skip Same Element

```python
if i != j:
```

Avoid multiplying current number with itself.

---

## 🔹 Multiply Remaining Elements

```python
product *= nums[j]
```

Example:

```python
2 * 3 * 4
```

---

## 🔹 Store Result

```python
result.append(product)
```

Add answer for current index.

---

# ⏱️ Complexity

## Time Complexity

```python
O(n²)
```

Because:
- outer loop → O(n)
- inner loop → O(n)

---

## Space Complexity

```python
O(1)
```

excluding output array.

---

# ❌ Problem

Works correctly…

BUT too slow for large inputs.

---

---

# 🧠 METHOD 2 — PREFIX + SUFFIX ARRAYS

## 🚀 Optimized Solution

---

# 🔥 Main Idea

Instead of recalculating products repeatedly:

Store:
- LEFT product
- RIGHT product

Then:

```python
answer[i] = left * right
```

---

# 🧠 PREFIX ARRAY

Stores product BEFORE current index.

---

## Example

Input:

```python
nums = [1,2,3,4]
```

Prefix:

```python
[1,1,2,6]
```

---

## Why?

```python
1
1
1*2 = 2
1*2*3 = 6
```

---

# 🧠 SUFFIX ARRAY

Stores product AFTER current index.

Suffix:

```python
[24,12,4,1]
```

---

## Why?

```python
2*3*4 = 24
3*4 = 12
4
1
```

---

# 🧠 Final Answer

Multiply:

```python
prefix[i] * suffix[i]
```

---

# ✅ Prefix + Suffix Code

```python
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)

        # Prefix array
        prefix = [1] * n

        # Suffix array
        suffix = [1] * n

        # Final answer
        answer = [1] * n


        # ----------------------------
        # BUILD PREFIX ARRAY
        # ----------------------------

        for i in range(1, n):

            prefix[i] = prefix[i - 1] * nums[i - 1]


        # ----------------------------
        # BUILD SUFFIX ARRAY
        # ----------------------------

        for i in range(n - 2, -1, -1):

            suffix[i] = suffix[i + 1] * nums[i + 1]


        # ----------------------------
        # BUILD FINAL ANSWER
        # ----------------------------

        for i in range(n):

            answer[i] = prefix[i] * suffix[i]

        return answer
```

---

# 🔍 Detailed Explanation

---

# 🔹 Prefix Logic

```python
prefix[i]
```

stores:
product of LEFT side elements.

---

# 🔹 Suffix Logic

```python
suffix[i]
```

stores:
product of RIGHT side elements.

---

# 🔹 Final Multiplication

```python
answer[i] = prefix[i] * suffix[i]
```

Combines left and right products.

---

# ⏱️ Complexity

## Time Complexity

```python
O(n)
```

---

## Space Complexity

```python
O(n)
```

Because:
- prefix array
- suffix array

---

---

# 🧠 METHOD 3 — OPTIMAL SPACE SOLUTION

# 🚀 REAL INTERVIEW SOLUTION

---

# 🔥 Main Idea

Instead of separate prefix/suffix arrays:

Use:
```python
answer array itself
```

to store prefix products.

Then traverse backwards using ONE suffix variable.

---

# 🧠 STEP-BY-STEP VISUAL

Input:

```python
nums = [1,2,3,4]
```

---

# STEP 1 — Build Prefix Inside Answer

Start:

```python
answer = [1,1,1,1]
```

---

## Forward Traversal

At i = 1:

```python
answer[1] = answer[0] * nums[0]
          = 1 * 1
          = 1
```

---

At i = 2:

```python
answer[2] = answer[1] * nums[1]
          = 1 * 2
          = 2
```

---

At i = 3:

```python
answer[3] = answer[2] * nums[2]
          = 2 * 3
          = 6
```

Now:

```python
answer = [1,1,2,6]
```

---

# STEP 2 — Traverse Backward Using Suffix

Start:

```python
suffix = 1
```

---

At i = 3:

```python
answer[3] *= suffix
6 * 1 = 6
```

Update suffix:

```python
suffix *= nums[3]
suffix = 4
```

---

At i = 2:

```python
answer[2] *= suffix
2 * 4 = 8
```

Update suffix:

```python
suffix = 12
```

---

At i = 1:

```python
1 * 12 = 12
```

---

At i = 0:

```python
1 * 24 = 24
```

Final:

```python
[24,12,8,6]
```

---

# ✅ Optimal Code

```python
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)

        # Final answer array
        answer = [1] * n


        # ---------------------------------
        # STEP 1: BUILD PREFIX PRODUCTS
        # ---------------------------------

        for i in range(1, n):

            answer[i] = answer[i - 1] * nums[i - 1]


        # ---------------------------------
        # STEP 2: MULTIPLY SUFFIX PRODUCTS
        # ---------------------------------

        suffix = 1

        # Traverse backwards
        for i in range(n - 1, -1, -1):

            answer[i] *= suffix

            suffix *= nums[i]


        return answer
```

---

# 🔍 Detailed Explanation

---

# 🔹 Prefix Stored Inside Answer

```python
answer[i]
```

initially stores LEFT product.

---

# 🔹 Suffix Variable

```python
suffix
```

stores RIGHT product dynamically.

---

# 🔹 Backward Traversal

```python
for i in range(n - 1, -1, -1):
```

Move:
RIGHT → LEFT

---

# 🔹 Final Multiplication

```python
answer[i] *= suffix
```

Combines:
- left product
- right product

---

# ⏱️ Complexity

## Time Complexity

```python
O(n)
```

---

## Extra Space Complexity

```python
O(1)
```

(Answer array does not count as extra space)

---

# 🏆 Comparison Table

| Method | Time | Space | Level |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Beginner |
| Prefix + Suffix Arrays | O(n) | O(n) | Intermediate |
| Optimal Space Solution | O(n) | O(1) | Advanced |

---

# 🚀 Important Concepts Learned

✅ Prefix Products  
✅ Suffix Products  
✅ Space Optimization  
✅ Forward Traversal  
✅ Backward Traversal  
✅ In-place Computation  
✅ Optimization Thinking  

---

# 🔥 AI Security Engineer Relevance

These concepts appear in:

- Tensor operations
- GPU computations
- Parallel processing
- Security analytics
- Malware scanning systems
- Efficient memory systems
- AI inference optimization

---

# 🧠 Final Takeaway

The goal is NOT just:
```python
"make code work"
```

The real goal is:
```python
"make code efficient"
```

That is REAL engineering mindset 🚀
