class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            fast = i
            slow = i

            for _ in range(len(nums)):

                fast = (fast + nums[fast]) % len(nums)
                if nums[fast] * nums[i] < 0:
                    break
                
                fast = (fast + nums[fast]) % len(nums)
                if nums[fast] * nums[i] < 0:
                    break
                
                slow = (slow + nums[slow]) % len(nums)
                nxt_slow = (slow + nums[slow])%len(nums)

                if slow == fast and slow != nxt_slow:
                    return True
        
        return False
        