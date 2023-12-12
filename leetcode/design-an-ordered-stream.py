class OrderedStream:

    def __init__(self, n: int):
        self.hashme = {}
        self.curr = 1
      
    
        

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.hashme[idKey]=value
        output = []
        
        while self.curr in self.hashme:
            output.append(self.hashme[self.curr])
            self.curr += 1
        
        return output
