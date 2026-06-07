# 0022 - Pattern 22
# https://takeuforward.org/plus/dsa/problems/pattern-22
# pattern: nested loops
# peeked: no
# brute:   O(n^2) - compute min distance from each border
# optimal: O(n^2) time, O(1) space - same, no better possible
#
# problem:
#   given an integer n, recreate the pattern below for any value of n.
#   for n=5:
#
#   5 5 5 5 5 5 5 5 5
#   5 4 4 4 4 4 4 4 5
#   5 4 3 3 3 3 3 4 5
#   5 4 3 2 2 2 3 4 5
#   5 4 3 2 1 2 3 4 5
#   5 4 3 2 2 2 3 4 5
#   5 4 3 3 3 3 3 4 5
#   5 4 4 4 4 4 4 4 5
#   5 5 5 5 5 5 5 5 5
#
#   print the pattern in the function given to you.


def pattern22(n):
    for i in range(n * 2 - 1):
        for j in range(n * 2 - 1):
            if n - i > 0:
                if j < i:
                    print(n - j, end=" ")
                elif j < ((n * 2 - 1) - i):
                    print(n - i, end=" ")
                else:
                    print((n - ((n * 2 - 2) - j)), end=" ")
            else:
                if i < j:
                    print((n - ((n * 2 - 2) - j)), end=" ")
                elif j < ((n * 2 - 2) - i):
                    print(n - j, end=" ")
                else:
                    print(i - (n - 2), end=" ")
        print()


def pattern22_better(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            print(n - min(i, j, (2 * n - 2) - i, (2 * n - 2) - j), end=" ")
        print()


if __name__ == "__main__":
    pattern22_better(5)
