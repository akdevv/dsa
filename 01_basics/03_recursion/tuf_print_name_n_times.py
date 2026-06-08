# 0024 - Print Name N Times Using Recursion
# https://takeuforward.org/recursion/print-name-n-times-using-recursion
# pattern: head recursion
# peeked: no
# brute:   O(N) - recurse N times
# optimal: O(N) time, O(N) space - same, recursion stack
#
# problem:
#   Given integer N, print your name N times using recursion.
#
#   example:
#     N=3 → Tony\nTony\nTony
#     N=1 → Tony


def solve(name: str, n: int):
    if n <= 0:
        return
    print(name)
    solve(name, n - 1)


if __name__ == "__main__":
    solve("Tony", 3)
