# 0001 - Selection Sort
# https://takeuforward.org/sorting/selection-sort-algorithm
# pattern: repeatedly select min from unsorted portion, swap to front
# peeked: hint
# brute:   O(n²) - nested loops, find min each pass
# optimal: O(n²) time, O(1) space - same; no better version exists
#
# problem:
#   sort an array in ascending order using selection sort
#
#   example:
#     [64, 25, 12, 22, 11] → [11, 12, 22, 25, 64]
#     [5, 3, 1, 2, 4]      → [1, 2, 3, 4, 5]


def solve(arr: list[int]):

    for i in range(len(arr)):
        # find the min ele
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap arr[min_idx] with arr[i]
        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp

    print(arr)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    solve(arr)
