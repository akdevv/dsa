# 0003 - Pattern 3
# https://takeuforward.org/plus/dsa/problems/pattern-3
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
#   12
#   123
#   1234
#   12345
#
#   print the pattern in the function given to you.


def pattern3(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        print()


if __name__ == "__main__":
    pattern3(5)
