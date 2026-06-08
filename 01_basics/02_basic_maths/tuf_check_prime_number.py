# Check for Prime Number
# https://takeuforward.org/plus/dsa/problems/check-for-prime-number
# pattern: if any divisor exists in 2..√n, not prime; else prime
# peeked: no
# brute:   O(n) time, O(1) space - check all divisors from 2 to n
# optimal: O(√n) time, O(1) space - check divisors only up to √n
#
# problem:
#   given an integer n, return true if it is prime, false otherwise.
#   a prime number has no divisors except 1 and itself.
#
#   example:
#     n = 5 → true
#     n = 8 → false


from math import isqrt


def solve(n: int) -> bool:
    if n <= 1:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def optimal(n: int) -> bool:
    if n <= 1:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    answer = optimal(11)
    print(answer)
