class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        player_distance = abs(target[0]) + abs(target[1]) 
        for ghost in ghosts:
            ghost_distance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])  
            if ghost_distance <= player_distance:
                return False

        return True

            
            