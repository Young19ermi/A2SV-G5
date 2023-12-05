class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        ans = ""
        string = indices.sort()
        solution = dict(zip(s, indices))
        for key,items in solution.items():
            x=sorted(solution.items())
            ans.append(solution[items])
        return ans
        """

        my_dict = dict(zip(indices, s))
        sorted_dict = dict(sorted(my_dict.items()))
        appended_string = ""
        for key, value in sorted_dict.items():
            appended_string += value
        return appended_string



"""
        ans = ""
        string = indices.sort()
        solution = dict(zip(s, indices))
        for key,items in solution.items():
            x=sorted(solution.items())
            ans.append(solution[items])
        return ans
        """