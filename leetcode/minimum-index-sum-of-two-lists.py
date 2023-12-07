class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexing = {rest: index for index, rest in enumerate(list1)}
        result = []
        curr_sum = 0
        min_sum = float('inf')
        for i, restaurant in enumerate(list2):
            if restaurant in indexing:
                curr_sum = i + indexing[restaurant]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [restaurant]
                elif curr_sum == min_sum:
                    result.append(restaurant)
        return result
 