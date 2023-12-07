class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = list(filter(lambda x:x<0, nums))
        right= list(filter(lambda x:x>0, nums))
        res = []
        i = 0
        j = 0
        while i < len(right) and j < len(left):
            res.append(right[i])
            res.append(left[j])
            i+=1
            j+=1
        while i < len(left)-1:
            i+=1
        while j < len(right)-1:
            j+=1
        return res
        

        

