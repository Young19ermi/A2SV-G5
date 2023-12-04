class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        initial = capacity
        count = 0
        total = 0
        for i in range(len(plants)):
            if capacity >= plants[i]:
                total += 1
            elif capacity < plants[i]:
                total += 2*(i) + 1
                capacity = initial
            capacity -= plants[i]
        return total
        