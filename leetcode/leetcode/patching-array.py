class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # init = [1]
        # n = 1
        # maxim = 0
        # unreachable = 0
        # patchs = 0
        # while unreachable < n-1:
        #     init.append(n+1) 
        #     init.append(sum(init) + 1)
        #     patchs += 1
        # return patchs
        miss, patchs = 1, 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i]<=miss:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                patchs += 1
        return patchs