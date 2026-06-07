# 0009 - Pattern 9
# https://takeuforward.org/plus/dsa/problems/pattern-9
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#       *
#      ***
#     *****
#    *******
#   *********
#   *********
#    *******
#     *****
#      ***
#       *
#
#   print the pattern in the function given to you.


def pattern9(n):
    for i in range(n):
        for _ in range(n - (i + 1)):
            print(" ", end="")
        print("*" * (i * 2 + 1))

    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        print("*" * ((n - i) * 2 - 1))


if __name__ == "__main__":
    pattern9(5)
