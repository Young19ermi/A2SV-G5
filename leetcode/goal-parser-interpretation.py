"""
class Solution:
    def interpret(self, command: str) -> str:
        string =list(command)
        i = 0
        res = ""
        while i < len(string)-1:
            if string[i:i+2] == "()":
                res += "o"
                i+=2
            elif string[i:i+4] == "(al)":
                res += "al"
                i+=4
            else:
                res += command[i]
                i+=1
        return res
        """
class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while i < len(command):
            if command[i:i+2] == "()":
                res += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                res += "al"
                i += 4
            else:
                res += command[i]
                i += 1
        return res


        