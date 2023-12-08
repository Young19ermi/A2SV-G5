class Solution:
    def printVertically(self, word: str) -> List[str]:
        
        
        words = word.split()
        max_length = max(len(word) for word in words)
        result = []

        for i in range(max_length):
            current_word = ''
            
            for word in words:
                if i < len(word):
                    current_word += word[i]
                else:
                    current_word += ' '
            
    
            result.append(current_word.rstrip())

        return result

            
        