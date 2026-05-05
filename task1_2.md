# Task 1-2: Step-by-step Divide-and-Conquer Trace

**Input:** `orders_change = [4, -2, 3, -1, 5, -3]`

---

## Figure 1. Recursion tree of the divide-and-conquer algorithm

```
                        [4, -2, 3, -1, 5, -3]
                       /                       \
              [4, -2, 3]                       [-1, 5, -3]
             /          \                     /            \
         [4, -2]        [3]              [-1, 5]          [-3]
         /      \                        /      \
       [4]      [-2]                  [-1]      [5]
    Step 1:4  Step 2:-2  Step 4:3  Step 6:-1  Step 7:5  Step 9:-3
```

> **Layout note:** Each leaf node carries a label `Step N: value` placed directly
> beneath the node so the tree stays readable.  Intermediate nodes carry their
> Step label to the right of the bracket in the same row (see table below).
> If the figure becomes too wide to fit on the page, split it into two halves
> (left subtree on one line, right subtree on the next) and use the table alone
> for the step numbers.

---

## Step-by-step results (place below or beside the figure)

| Step | Subarray      | Max subarray sum |
|------|---------------|-----------------|
| 1    | `[4]`         | **4**           |
| 2    | `[-2]`        | **-2**          |
| 3    | `[4, -2]`     | **4**           |
| 4    | `[3]`         | **3**           |
| 5    | `[4, -2, 3]`  | **5**           |
| 6    | `[-1]`        | **-1**          |
| 7    | `[5]`         | **5**           |
| 8    | `[-1, 5]`     | **5**           |
| 9    | `[-3]`        | **-3**          |
| 10   | `[-1, 5, -3]` | **5**           |

---

## Crossing-sum calculation (root level)

`mid = 2` (value `3`); left half indices 0–2, right half indices 3–5.

```
Left suffix maximum (start at mid, scan leftward):
  i=2: total = 3          → best = 3
  i=1: total = 3+(-2) = 1 → best = 3
  i=0: total = 1+4    = 5 → best = 5   ← left suffix max = 5

Right prefix maximum (start at mid+1, scan rightward):
  i=3: total = -1         → best = -1
  i=4: total = -1+5   = 4 → best = 4   ← right prefix max = 4
  i=5: total = 4+(-3) = 1 → best = 4

Crossing sum = 5 + 4 = 9
```

**Final answer = max(left max, right max, crossing max) = max(5, 5, 9) = 9**

---

## Caption (place directly under the figure in Word)

> **Figure 1.** Divide-and-conquer recursion tree for
> `orders_change = [4, -2, 3, -1, 5, -3]`.  
> The array is recursively split into two halves until single elements are
> reached (Steps 1, 2, 4, 6, 7, 9).  Intermediate results are merged bottom-up
> (Steps 3, 5, 8, 10).  The maximum subarray sum crossing the midpoint is 9,
> obtained from the subarray `[4, -2, 3, -1, 5]`.  Therefore the final answer
> is **9**.

---

## Word layout recommendation

1. **Heading:** `Task 1-2`  (Bold, Heading 2 style)
2. **Figure block:** paste the monospaced recursion tree above using
   **Consolas** or **Courier New**, 10 pt.  
   — *Option A (clean):* keep only the tree structure in the figure; put
   Step labels in the table below.  
   — *Option B (compact):* annotate each node with `Step N: value` directly
   beside the bracket as shown in the tree above.
3. **Table:** insert the 10-row step table immediately below the figure.
4. **Crossing-sum block:** place the crossing-sum calculation in a `code` block
   or indented paragraph.
5. **Caption:** italic, centered, 9 pt.
6. **Explanation paragraph:** one short paragraph (3–4 sentences) summarising
   the algorithm — copy from the caption and expand if needed.
