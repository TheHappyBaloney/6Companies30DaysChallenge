# 324. Wiggle Sort II
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2 
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
