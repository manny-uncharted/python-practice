class Solution:
    def romanToInt(self, s: str) -> int:
        """
        if encouter m:
         -- update sum
         -- move pointer to next
        if encounter c:
           -- check if next value and next value is d:
               -- add 400 to sum
               -- move pointer by 2
           -- check if next value and next value is m:
               -- add 900 to sum
               -- move pointer by 2
         if encounter x:
            -- check if next value and next value is l:
                 -- add 40 to sum
                 -- move pointer by 2
            -- check if next value and next value is c:
                 -- add 100 to sum
                 -- move pointer by 2
         if encounter I:
             -- check if next val and next val is V:
                 -- add 4 to sum
                 -- move pointer by 2
             -- check if next val and next val is X:
               - -- add 9 to sum
               --- move pointer by 2
         else:
             sum + map.get(value of string)
        """
        vals_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        p1 = 0
        sum = 0
        while p1 < len(s):
            if s[p1] == 'M':
                sum += 1000
                p1 +=1
            elif s[p1] == 'C':
                if (p1+1) < len(s) and s[p1+1] == 'D':
                    sum += 400
                    p1 +=2
                elif (p1+1) < len(s) and s[p1+1] == 'M':
                     sum += 900
                     p1 += 2
                else:
                    sum +=100
                    p1 +=1
            elif s[p1] == 'X':
                if (p1+1) < len(s) and s[p1+1] == 'L':
                    sum += 40
                    p1 +=2
                elif (p1+1) < len(s) and s[p1+1] == 'C':
                     sum += 90
                     p1 += 2
                else:
                    sum += 10
                    p1 +=1
            elif s[p1] == 'I':
                if (p1+1) < len(s) and s[p1+1] == 'V':
                    sum += 4
                    p1 +=2
                elif (p1+1) < len(s) and s[p1+1] == 'X':
                     sum += 9
                     p1 += 2
                else:
                    sum +=1
                    p1 +=1
            else:
                sum += vals_map.get(s[p1])
                p1 +=1
        return sum