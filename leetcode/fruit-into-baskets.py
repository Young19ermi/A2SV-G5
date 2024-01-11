from collections import defaultdict

class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        i = 0
        countme = defaultdict(int)
        for j in range(len(nums)):
            countme[nums[j]] = 1 + countme.get(nums[j], 0)
            while len(countme.keys()) > 2 and i < len(nums):
                countme[nums[i]] -= 1
                if countme[nums[i]] == 0:
                    del countme[nums[i]]
                count -= 1
                i += 1
            count += 1
            maximum = max(count, maximum)
        return maximum

# class Solution:
#     def totalFruit(self, nums: List[int]) -> int:
#         count = 0
#         maximum = 0
#         i = 0
#         countme = defaultdict(int)
#         for j in range(len(nums)):
#             countme[nums[j]] = 1 + countme.get(nums[j], 0)
#             while len(countme.keys()) > 2 and i < len(nums):
#                 countme[nums[i]] -= 1
#                 del countme[nums[i]]
#                 i += 1
#                 count -= 1
#             count += 1
#             maximum = max(count, maximum)
#         return maximum



# for j in range(1,len(nums)):
        #     if nums[j] != nums[i]:
        #         offset += 1
        #         if offset >= 2:
        #             i += 1
        #             count -= 1
        #             maximum = max(maximum, count)
        #     else:
        #         count += 1
                
        # return maximum


