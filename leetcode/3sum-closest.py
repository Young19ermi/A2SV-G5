class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right :
                total = nums[i] + nums[right] + nums[left]
                print(total)
                if abs(total - target) < abs(closest - target):
                    closest = total
                    print(closest)
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
                   
        return closest      