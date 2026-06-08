# 0007 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# pattern: reverse digits using string slicing, apply sign separately
# peeked: no
# brute:   O(log n) time, O(log n) space - string reverse, check overflow after
# optimal: O(log n) time, O(log n) space - same as brute; math approach would be O(1) space
#
# problem:
#   given a signed 32-bit integer x, return x with its digits reversed.
#   if reversing causes overflow outside [-2^31, 2^31 - 1], return 0.
#   assume 64-bit integers are not available.
#
#   example:
#     x = 123  → 321
#     x = -123 → -321
#     x = 120  → 21  (leading zero dropped)


def solve(n: int) -> int:
    sign = -1 if n < 0 else 1
    rev_num = int(str(abs(n))[::-1]) * sign

    if rev_num < -(2**31) or rev_num > 2**31 - 1:
        return 0

    return rev_num


if __name__ == "__main__":
    rev_num = solve(-456)
    print(rev_num)
