class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in a and a[comp] != i:
                return [i, a[comp]]
        return []