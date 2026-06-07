# 0004 - Pattern 4
# https://takeuforward.org/plus/dsa/problems/pattern-4
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   1
#   22
#   333
#   4444
#   55555
#
#   print the pattern in the function given to you.


def pattern4(n):
    for i in range(n):
        for _ in range(i + 1):
            print(i + 1, end="")
        print()


if __name__ == "__main__":
    pattern4(4)
