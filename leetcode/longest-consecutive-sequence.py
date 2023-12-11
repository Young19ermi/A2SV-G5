class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashme = sorted(list(set(nums)))
        
        count = 1
        maxme = 1
        for i in range(1,len(hashme)):
            if hashme[i] - hashme[i-1] == 1:
                count += 1
                maxme =max(maxme, count)
            else:
                count = 1
        return maxme  if hashme != [] else 0


"""
        hashme = {}
        for num in nums:
            if num in hashme:
                hashme[num] += 1
            else:
                hashme[num] = 1
        for number, count in hashme.items():
            if count != 1:
                continue
            else:
                if count == 1:
                    number
                    """ 

        

"""
        hashme = {}
        for num in nums:
            if num in hashme:
                hashme[num] += 1
            else:
                hashme[num] = 1
        for number, count in hashme.items():
            if count != 1:
                continue
            else:
                if count == 1:
                    number
                    """ 

        