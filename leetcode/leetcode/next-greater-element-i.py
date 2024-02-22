class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = 0
        res = []
        for n in nums1:
            for j in range(len(nums2)):
                if n == nums2[j]:
                    while j < len(nums2):
                        if nums2[j] > n:
                            ans += nums2[j]
                            break
                        else:
                            j+=1
                    if ans == 0:
                        res.append(-1)
                    else:
                        res.append(ans)
                    ans = 0
                
        return res