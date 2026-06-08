# 0009 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# pattern: reverse string and compare with original
# peeked: no
# brute:   O(log n) time, O(log n) space - convert to string, reverse, compare
# optimal: O(log n) time, O(log n) space - same; math approach would save space
#
# problem:
#   given an integer x, return true if x is a palindrome, false otherwise.
#   a palindrome reads the same left to right and right to left.
#   negative numbers are never palindromes.
#
#   example:
#     x = 121  → true   (121 reversed is 121)
#     x = -121 → false  (-121 reversed is 121-)
#     x = 10   → false  (10 reversed is 01)


def solve(x: int) -> bool:
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    answer = solve(-121)
    print(answer)
