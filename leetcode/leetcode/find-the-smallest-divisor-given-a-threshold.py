
class Solution:
    def smallestDivisor(self, nums: List[int], target: int) -> int:
        
        left = 1
        right = max(nums)

        #Life saver function
        def solve(m):
            return sum(ceil(num / m) for num in nums)

        while left < right:
            mid = (left + right) // 2
            if solve(mid) > target:
                left = mid + 1
            else:
                right = mid
        
        return left
        # while i < j:
        #     mid = (i+j) // 2
        #     if solve(mid) < target:
        #         j = mid
        #     else:
        #         i = mid+1
        # return j 
        
        

        # i = 0
        # j = len(numbers)-1
        # might = float('inf')
        # while i <= j:
        #     mid = (i+j) // 2
        #     print(numbers[mid])
        #     if solve(nums,mid) > target:
        #         j = mid -1
        #         i = mid + 1
        #     else:
        #         #might = min(might, mid)
        #         i = mid + 1
        #        # might = min(might, mid)
        # might = min(might, mid)
        # return might