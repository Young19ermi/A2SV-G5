from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []

        def solve(i, cur, tot):
            if tot == target:
                arr.append(cur.copy())
                return

            if i >= len(nums) or tot > target:
                return

           
            cur.append(nums[i])
            solve(i, cur, tot + nums[i])

            
            cur.pop()
            solve(i + 1, cur, tot)

        solve(0, [], 0)
        return arr
