# 0003 - Insertion Sort
# https://takeuforward.org/data-structure/insertion-sort-algorithm/
# pattern: pick element, shift backward until in correct position in sorted prefix
# peeked: hint
# best:    O(n) - already sorted, early break fires every pass
# avg:     O(n²) - random order
# worst:   O(n²) time, O(1) space - reverse sorted
#
# problem:
#   sort an array in ascending order using insertion sort
#
#   example:
#     [64, 25, 12, 22, 11] → [11, 12, 22, 25, 64]
#     [5, 3, 1, 2, 4]      → [1, 2, 3, 4, 5]


def solve(arr: list[int]):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                # swap
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
            else:
                break

    print(arr)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    solve(arr)
