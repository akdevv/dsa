# 0001 - Count Digits in a Number
# https://takeuforward.org/data-structure/count-digits-in-a-number
# pattern: log base 10 of n gives number of digits; loop simulates it via repeated division
# peeked: no
# brute:   O(log n) time, O(log n) space - convert to string, return length
# optimal: O(log n) time, O(1) space - divide by 10 until < 10, count steps
#
# problem:
#   given an integer n, return the number of digits in n.
#   no leading zeroes, except when n is 0 itself.
#
#   example:
#     n = 4  → 1
#     n = 14 → 2


def solve(n: int) -> int:
    digits = 1
    while n >= 10:
        n = n // 10
        digits += 1
    return digits


if __name__ == "__main__":
    digits = solve(1000)
    print(digits)
