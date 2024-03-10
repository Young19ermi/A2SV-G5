class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        res = []

        for n in nums1:
            i = 0
            j = len(nums2) - 1

            while i <= j:
                mid = (i + j) // 2

                if n == nums2[mid]:
                    if n not in res:  
                        res.append(n)
                    break  
                elif n < nums2[mid]:
                    j = mid - 1
                else:
                    i = mid + 1

        return res

