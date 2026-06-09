# Reverse a given Array
# https://takeuforward.org/data-structure/reverse-a-given-array
# pattern: recursion, swap left & right, move inward
# peeked: yes
# brute:   O(n) time, O(n) space - recursive swaps, stack depth n


def solve(arr: list, left: int, right: int):
    if left >= right:
        return

    # swap
    arr[left], arr[right] = arr[right], arr[left]

    solve(arr, left + 1, right - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    solve(arr, 0, len(arr) - 1)
    print(arr)
