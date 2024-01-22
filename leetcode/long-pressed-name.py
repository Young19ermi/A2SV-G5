class Solution(object):
    def isLongPressedName(self, name, typed):
        
        name_idx = 0
        typed_idx = 0
        while name_idx <= len(name) and typed_idx < len(typed):
            if name_idx < len(name) and typed[typed_idx] == name[name_idx]:
                typed_idx += 1
                name_idx += 1
            elif typed[typed_idx] == name[name_idx-1] and name_idx != 0:
                typed_idx += 1
            else:
                return False
            
        return name_idx == len(name) and typed_idx == len(typed)
        # count = Counter(typed)
        # name_count = Counter(name)
        # for j in range(len(name)):
        #     if name_count[name[j]] > count[name[j]]:
        #         return False
        #         break
        # letters = list(set(typed))
        # names = list(set(name))
        # if len(letters) != len(names):
        #     return False
        # for i in range(len(letters)):
        #     if letters[i] != names[i]:
        #         return False
        # return True
        # i = 0
        # while j < len(typed):
        #     while True:
        #         if names[i] == typed[j]:
        #             j += 1
        #         i += 1
        #         count += 1
        #         if count >= 1:
        #             return False
        #     return True