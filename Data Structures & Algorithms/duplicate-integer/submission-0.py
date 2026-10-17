class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        n = len(nums)

        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False