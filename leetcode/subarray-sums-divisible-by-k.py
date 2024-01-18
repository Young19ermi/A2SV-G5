class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashme = {0:1}
        total = 0
        rem = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            if rem in hashme.keys():
                count += hashme[rem]
                hashme[rem] += 1
           
            else:
                hashme[rem] = 1
        print(hashme)
        return count


        
        