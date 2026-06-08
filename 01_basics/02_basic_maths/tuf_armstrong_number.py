# Armstrong Number
# https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not
# pattern: find len of number, sum each digit raised to power of digit count, compare to n
# peeked: no
# brute:   O(log n) time, O(log n) space - convert to string, iterate digits, sum powers
# optimal: O(log n) time, O(1) space - same logic using modulo instead of string conversion
#
# problem:
#   given an integer n, return true if it is an armstrong number, false otherwise.
#   armstrong number: sum of each digit raised to the power of number of digits == n.
#
#   example:
#     n = 153 → true   (1^3 + 5^3 + 3^3 = 153)
#     n = 371 → true   (3^3 + 7^3 + 1^3 = 371)
#     n = 123 → false


def solve(n: int) -> bool:
    k = len(str(n))
    total = 0
    for i in range(k):
        total += int(str(n)[i]) ** k
    return n == total


if __name__ == "__main__":
    answer = solve(153)
    print(answer)
