class Solution:
    def romanToInt(self, s: str) -> int:
        
        number = 0
        
        symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        i = 0
        
        while i < len(s):
            current_num = symbols[s[i]]
            next_num = symbols[s[i + 1]] if (i + 1) < len(s) else None
            
            if next_num and current_num < next_num:
                number += (next_num - current_num)
                i += 2
            else:
                number += current_num
                i += 1
            
            
        return number
