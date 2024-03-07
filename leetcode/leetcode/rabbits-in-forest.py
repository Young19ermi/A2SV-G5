class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counted_rabbit = defaultdict(int)
        min_num_rabbits = 0

        for ans in answers:    
            if ans not in counted_rabbit or counted_rabbit[ans] == ans + 1:
                min_num_rabbits += ans + 1
                counted_rabbit[ans] = 1
            else:
                counted_rabbit[ans] += 1        
        return min_num_rabbits
        