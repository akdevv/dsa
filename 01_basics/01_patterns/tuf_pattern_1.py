# TUF Pattern 1
# https://takeuforward.org/plus/dsa/problems/pattern-1
# pattern: solid N×N rectangle of stars
# peeked: no
# brute:   O(N²) - print N rows of N stars
# optimal: O(N²) time, O(1) space - no better possible

def pattern(n: int):
    for _ in range(n):
        print ("*" * n)


if __name__ == "__main__":
    pattern(5)
