class Solution:
    def longestPalindrome(self, s: str) -> int:
        cc = Counter(s)
        l = 0
        has_o = False

        for c in cc.values():
            l += (c // 2) * 2

            if c % 2 == 1:
                has_o = True

        return l + 1 if has_o else l