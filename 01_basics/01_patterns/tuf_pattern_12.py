# 0012 - Pattern 12
# https://takeuforward.org/plus/dsa/problems/pattern-12
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   1        1
#   12      21
#   123    321
#   1234  4321
#   1234554321
#
#   print the pattern in the function given to you.


def pattern12(n):
    for i in range(n):
        for j in range(n * 2):
            if j <= i:
                print(j + 1, end="")
            elif j < (n * 2 - i - 1):
                print(" ", end="")
            else:
                print((n * 2 - j), end="")
        print()


if __name__ == "__main__":
    pattern12(5)
