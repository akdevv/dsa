# 0002 - Bubble Sort
# https://takeuforward.org/data-structure/bubble-sort-algorithm/
# pattern: repeatedly bubble largest to end; stop early if no swaps
# peeked: hint
# best:    O(n) - already sorted, no swaps in first pass
# avg:     O(n²) - random order
# worst:   O(n²) time, O(1) space - reverse sorted
#
# problem:
#   sort an array in ascending order using bubble sort
#
#   example:
#     [64, 25, 12, 22, 11] → [11, 12, 22, 25, 64]
#     [5, 3, 1, 2, 4]      → [1, 2, 3, 4, 5]


def solve(arr: list[int]):
    n = len(arr)

    for i in range(n):
        have_swaped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                have_swaped = True
        if not have_swaped:
            break
    print(arr)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    solve(arr)
