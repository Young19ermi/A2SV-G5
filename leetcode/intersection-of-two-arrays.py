class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        res = 0
        for num in nums1:
            set1.add(num) 
        for num in nums2:
            set2.add(num)
        res= set1 & set2
        return res
        