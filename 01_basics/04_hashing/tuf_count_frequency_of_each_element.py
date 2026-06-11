# 0024 - Count Frequency of Each Element in the Array
# https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array
# pattern: pre-store frequencies and fetch
# peeked: no
# brute:   O(n^2) - nested loop, count each element by scanning full array
# optimal: O(n) time, O(n) space - single pass with hash map
#
# problem:
#   Given an array, find the number of occurrences of each element.
#
#   example:
#     [10, 5, 10, 15, 10, 5] → 10: 3, 5: 2, 15: 1
#     [2, 2, 3, 4, 4, 2]     → 2: 3, 3: 1, 4: 2


def solve(arr: list):
    freq_arr = dict()

    for x in arr:
        if x not in freq_arr:
            freq_arr[x] = 0
        freq_arr[x] += 1

    # print frequencies
    for k, v in freq_arr.items():
        print(k, v)


if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]
    solve(arr)
