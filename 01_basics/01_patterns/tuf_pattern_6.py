# 0006 - Pattern 6
# https://takeuforward.org/plus/dsa/problems/pattern-6
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   12345
#   1234
#   123
#   12
#   1
#
#   print the pattern in the function given to you.


def pattern6(n):
    for i in range(n):
        for j in range(n - i):
            print(j + 1, end="")
        print()


if __name__ == "__main__":
    pattern6(5)
