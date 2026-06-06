# Pattern: Sliding Window

**trigger** — contiguous subarray/substring + "longest/shortest/max/min/count" under a constraint. anything asking about a window over a sequence.

**skeleton**
```python
def sliding_window(arr):
    left = 0
    state = 0            # running sum / counter / freq map
    best = 0
    for right in range(len(arr)):
        # 1. expand: add arr[right] to state
        # 2. shrink while window invalid:
        while invalid(state):
            # remove arr[left] from state
            left += 1
        # 3. record answer for current valid window
        best = max(best, right - left + 1)
    return best
```

**examples**
- 0003 Longest Substring Without Repeating Characters
- 0076 Minimum Window Substring
- 0209 Minimum Size Subarray Sum

**gotchas**
- fixed-size window vs variable-size — variable uses the while-shrink, fixed just slides.
- decide what "state" is BEFORE coding (sum? count? freq dict?).
