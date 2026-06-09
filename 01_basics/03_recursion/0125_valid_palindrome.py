# 0125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome
# pattern: loop + clean to alphanumeric, compare with reverse
# peeked: no
# brute:   O(n) time, O(n) space - clean string, compare to reversed
#
# problem:
#   Given string s, return true if it's a palindrome after lowercasing
#   and removing all non-alphanumeric characters.
#
#   example:
#     "A man, a plan, a canal: Panama" → True
#     "race a car" → False
#     " " → True


def solve(s: str):
    # chr(97) - chr(122) == a-z

    cleaned = ""
    for letter in s.lower():
        if (ord(letter) >= 97 and ord(letter) <= 122) or (
            ord(letter) >= 48 and ord(letter) <= 57
        ):
            cleaned += letter
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    answer = solve("A man, a plan, a canal: Panama")
    print(answer)
