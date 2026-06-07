# 0011 - Pattern 11
# https://takeuforward.org/plus/dsa/problems/pattern-11
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
#   01
#   101
#   0101
#   10101
#
#   print the pattern in the function given to you.


def pattern11(n):
    for i in range(n):
        for j in range(i + 1):
            if ((i + j) % 2) == 0:
                print(1, end="")
            else:
                print(0, end="")
        print()


if __name__ == "__main__":
    pattern11(5)
