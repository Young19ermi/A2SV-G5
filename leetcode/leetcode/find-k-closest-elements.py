class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        
       
        i = 0
        j = len(nums)-1
        while i <= j:
        
            mid = (i+j)//2
            if nums[mid] <= x:
                i = mid+1
            else:
                j = mid -1
        before = j
        after = j + 1
        res = []
        print(before,after)
        for i in range(k):
            if after >= len(nums):
                res.append(nums[before])
                before -= 1
            elif before < 0:
                res.append(nums[after])
                after += 1
            else:
                if x -nums[before] <= nums[after] - x:
                    res.append(nums[before])
                    before -= 1
                else:
                    res.append(nums[after])
                    after += 1
        res.sort()    
        return res
