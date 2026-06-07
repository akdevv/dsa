# 0001 - Pattern 1
# https://takeuforward.org/plus/dsa/problems/pattern-1
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - nested loops
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   *****
#   *****
#   *****
#   *****
#   *****
#
#   print the pattern in the function given to you.

def pattern(n: int):
    for _ in range(n):
        print ("*" * n)


if __name__ == "__main__":
    pattern(5)
