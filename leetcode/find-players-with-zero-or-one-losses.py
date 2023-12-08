class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        player_losses = defaultdict(int)
        
        for winner, loser in matches:
            player_losses[winner] += 0
            player_losses[loser] += 1
        
        result = [[], []]
        for player, losses in player_losses.items():
            if losses == 0:
                result[0].append(player)
            elif losses == 1:
                result[1].append(player)
        
        result[0].sort()
        result[1].sort()
        
        return result

        