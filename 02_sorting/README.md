# Sorting

Seven algorithms, top to bottom. Each has one core idea — learn the idea, the code follows.

| #   | Algorithm           | Best       | Avg        | Worst      | Space    | Stable |
| :-- | :------------------ | :--------- | :--------- | :--------- | :------- | :----- |
| 1   | Selection           | O(n²)      | O(n²)      | O(n²)      | O(1)     | no     |
| 2   | Bubble              | O(n)       | O(n²)      | O(n²)      | O(1)     | yes    |
| 3   | Insertion           | O(n)       | O(n²)      | O(n²)      | O(1)     | yes    |
| 4   | Merge               | O(n log n) | O(n log n) | O(n log n) | O(n)     | yes    |
| 5   | Quick               | O(n log n) | O(n log n) | O(n²)      | O(log n) | no     |
| 6   | Recursive Bubble    | O(n)       | O(n²)      | O(n²)      | O(n)\*   | yes    |
| 7   | Recursive Insertion | O(n)       | O(n²)      | O(n²)      | O(n)\*   | yes    |

\* recursive versions add O(n) call-stack space.

---

## 1. Selection Sort

Pick the smallest, put it first. Repeat on what's left.

- Scan the unsorted part for the minimum element.
- Swap it to the front of the unsorted part.
- Left side grows sorted, right side shrinks.
- Takes n−1 passes.

**Cost:** O(n²) always — even a sorted array gets fully scanned. No early exit.
**Not stable:** the long-distance swap can jump an equal element past its twin.

---

## 2. Bubble Sort

Biggest element bubbles to the end each pass.

- Compare adjacent pairs (0,1), (1,2), … If left > right, swap.
- After one full pass the largest element sits at the end.
- Next pass ignores the last element, then the last two, and so on.

**Trick:** if a whole pass makes zero swaps, the array is already sorted — stop early. That gives the O(n) best case.

---

## 3. Insertion Sort

Build a sorted prefix, insert each new element into place — like sorting a hand of cards.

- Left side is kept sorted. Take the next element.
- Shift larger elements in the sorted prefix one step right.
- Drop the element into the hole that opens up.

**Best case O(n):** on a sorted array each element is already in place, the inner shift never fires. Great on nearly-sorted data.

---

## 4. Merge Sort

Divide and conquer. Split, sort halves, merge.

- Recursively split the array in half until pieces are size 1 (already sorted).
- Merge two sorted halves into one with a two-pointer walk.
- Every level does O(n) merge work, there are log n levels → O(n log n).

**Cost:** O(n log n) guaranteed — input order doesn't matter. Needs O(n) temp space for the merge.

---

## 5. Quick Sort

Pick a pivot, partition around it, recurse on both sides.

- Choose a pivot (first, last, random, or median).
- Partition: smaller goes left, larger goes right. Pivot lands in its final spot.
- Recurse on the left and right partitions.

**In-place** — no temp array, unlike merge sort. That's its edge.
**Worst case O(n²):** a bad pivot (e.g. always the max on already-sorted input) makes lopsided partitions. Random pivot dodges this in practice.

---

## 6. Recursive Bubble Sort

Same bubble sort, recursion replaces the outer loop.

- One recursive call = one full pass bubbling the largest to the end.
- Recurse on the array minus its last element.
- Base case: size 1, or a pass with no swaps → already sorted.

Same O(n²) time, recursive framing. Adds call-stack space.

---

## 7. Recursive Insertion Sort

Same insertion sort, recursion replaces the outer loop.

- Recursively sort the first i elements.
- Then insert element i into that sorted prefix by shifting.
- Base case: prefix of size 1 is trivially sorted.

Same O(n²) time, recursive framing. Adds call-stack space.

---

## Which one, when?

- **Small / nearly-sorted** → insertion sort. Cheap, O(n) best case.
- **Need guaranteed O(n log n) or stability** → merge sort.
- **General fast in-place sort** → quick sort (what most libraries use, often hybridized).
- **Selection / bubble** → learning tools, rarely used for real.
