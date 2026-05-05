# DTS103 Assignment – Maximum Subarray Sum (Divide and Conquer)

---

## Task 1-1: Divide-and-Conquer Implementation

### Python Code (with English comments)

```python
def max_order_increase(orders_change):
    # If the array is empty, there is no subarray sum
    if not orders_change:
        return 0

    def helper(left, right):
        # Base case: only one element in the current range
        if left == right:
            return orders_change[left]

        # Divide the array into two halves
        mid = (left + right) // 2

        # Recursively find the maximum subarray sum in the left half
        left_max = helper(left, mid)

        # Recursively find the maximum subarray sum in the right half
        right_max = helper(mid + 1, right)

        # Find the maximum suffix sum on the left side that ends at mid
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += orders_change[i]
            left_sum = max(left_sum, current_sum)

        # Find the maximum prefix sum on the right side that starts at mid + 1
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += orders_change[i]
            right_sum = max(right_sum, current_sum)

        # The best subarray crossing the middle
        cross_max = left_sum + right_sum

        # Return the best among left, right, and crossing subarrays
        return max(left_max, right_max, cross_max)

    return helper(0, len(orders_change) - 1)
```

### Test

```python
orders_change = [4, -2, 3, -1, 5, -3]
print(max_order_increase(orders_change))
# Output: 9
```

The function was tested with `orders_change = [4, -2, 3, -1, 5, -3]`, and the output is `9`, which matches the expected maximum subarray sum.

---

## Task 1-2: Step-by-Step Explanation for `[4, -2, 3, -1, 5, -3]`

### How to Present This Figure in Your Report

**Recommended report layout:**

1. **Heading line** (above the figure):
   > **Task 1-2: Step-by-step explanation for `orders_change = [4, -2, 3, -1, 5, -3]`**

2. **The figure itself** — a recursion/division diagram (see below).

3. **Caption line** (below the figure, ready to paste):
   > *Figure 1. Recursion tree of the divide-and-conquer algorithm on input `[4, -2, 3, -1, 5, -3]`. The maximum contiguous subarray sum is 9, achieved by the subarray `[4, -2, 3, -1, 5]`.*

4. **One-paragraph description** (paste after the caption):
   > The array is split at the midpoint into two halves: `[4, -2, 3]` (left) and `[-1, 5, -3]` (right). The algorithm recurses into each half, computing the maximum subarray sum for the left half (5, from `[4, -2, 3]`) and the right half (5, from `[5]`). It then computes the maximum crossing sum by finding the best suffix of the left half (4 + (−2) + 3 = 5) and the best prefix of the right half (−1 + 5 = 4), giving a crossing sum of 5 + 4 = 9. Taking the maximum of 5, 5, and 9 yields the final answer of **9**.

---

### Recursion Tree Diagram

The figure to include in your report should look like this:

```
Input: [4, -2, 3, -1, 5, -3]
                │
        ┌───────┴────────┐
  [4, -2, 3]         [-1, 5, -3]
      │                   │
  ┌───┴───┐           ┌───┴───┐
[4, -2]  [3]       [-1, 5]  [-3]
  │                    │
┌─┴─┐               ┌─┴─┐
[4] [-2]           [-1] [5]

Left half max  = 5   (subarray [4, -2, 3])
Right half max = 5   (subarray [5])
Cross max      = 9   (left suffix 5 + right prefix 4)
                         ↑                    ↑
                   4+(−2)+3=5          (−1)+5=4

Final answer = max(5, 5, 9) = 9
Optimal subarray = [4, -2, 3, -1, 5]
```

---

### What the Figure Must Show

| Element | Details |
|---|---|
| Original array | `[4, -2, 3, -1, 5, -3]` at the top |
| Split levels | Each recursive split shown as branches |
| Per-level max values | The maximum sum returned at each node |
| Crossing calculation | Left suffix max + Right prefix max = 5 + 4 = 9 |
| Final answer | `max(5, 5, 9) = 9` with the winning subarray highlighted |

---

### Ready-to-Paste Caption (English)

> **Figure 1.** Recursion tree of the divide-and-conquer algorithm applied to `orders_change = [4, -2, 3, -1, 5, -3]`. The array is split into halves at each level; the left-half maximum is 5, the right-half maximum is 5, and the crossing maximum is 9 (left suffix 5 + right prefix 4). The final answer is **9**, corresponding to the subarray `[4, -2, 3, -1, 5]`.

---

### Summary Table of All Sub-results

| Sub-array | Max subarray sum | Source |
|---|---|---|
| `[4]` | 4 | base case |
| `[-2]` | −2 | base case |
| `[4, -2]` | 4 | left max |
| `[3]` | 3 | base case |
| `[4, -2, 3]` | **5** | crossing: 2+3 |
| `[-1]` | −1 | base case |
| `[5]` | 5 | base case |
| `[-1, 5]` | 5 | right max |
| `[-3]` | −3 | base case |
| `[-1, 5, -3]` | **5** | left max |
| `[4,-2,3,-1,5,-3]` | **9** | crossing: 5+4 |
