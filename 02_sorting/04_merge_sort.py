# 0004 - Merge Sort
# https://takeuforward.org/data-structure/merge-sort-algorithm/
# pattern: divide array in half recursively, merge sorted halves
# peeked: hint
# best:    O(n log n) - always divides and merges regardless of input
# avg:     O(n log n) - same
# worst:   O(n log n) time, O(n) space - tmp array for merging
#
# problem:
#   sort an array in ascending order using merge sort
#
#   example:
#     [64, 25, 12, 22, 11] → [11, 12, 22, 25, 64]
#     [5, 3, 1, 2, 4]      → [1, 2, 3, 4, 5]


def merge(arr: list[int], low: int, mid: int, high: int):
    tmp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1

    while left <= mid:
        tmp.append(arr[left])
        left += 1
    while right <= high:
        tmp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i - low]


def merge_sort(arr: list[int], low: int, high: int):
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    merge_sort(arr, 0, len(arr) - 1)

    print(arr)
