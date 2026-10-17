class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = -1
        count = 0
        for n in nums:
            if count == 0:
                c = n
                count = 1
            elif c == n:
                count += 1
            else:
                count -= 1
        
        total = sum(1 for n in nums if n == c)
        left = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == c:
                left += 1
            if left * 2 > i + 1:
                right = total - left
                if right * 2 > n - 1 - i:
                    return i
        return -1