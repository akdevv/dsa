# 0002 - Pattern 2
# https://takeuforward.org/plus/dsa/problems/pattern-2
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   *
#   **
#   ***
#   ****
#   *****
#
#   print the pattern in the function given to you.


def pattern2(n):
    for i in range(n):
        print("*" * (i + 1))


if __name__ == "__main__":
    pattern2(4)
