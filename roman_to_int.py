class Solution:
    def romanToInt(self, s: str) -> int:
        s_length = len(s)
        opts = ["I", "V", "X", "L", "C", "D", "M"]
        nums = []
        
        
        skip_next = False
        for i in range(s_length):
            ch = s[i]
            if not ch in opts:
                raise Exception("Invalid character")

            # "double" continue guard
            if skip_next:
                print("inside skip_next")
                # First, reset skip_next
                skip_next = False
                
                continue
                
            prev = s[i - 1]
            
            print("i", i)
            check_next = ""
            check_second = ""
            print("S LENGTH", s_length)
            if s_length > (i + 1):
                print(i)
                print(s[i + 1])
                print('here 1')
                check_next = s[i + 1]

            if s_length > (i + 2):
                print(i + 2)
                print(s[i + 2])
                print('here 2')
                check_second = s[i + 2]
            print("test1", ch)
            print("test2", check_next)
            print("test3", check_second) 
            # The multiple in a row items must be checked first
            
            # check for IV combo 4
            if ch == "I" and check_next == "V":
                num = 4
                skip_next = True
            # check for IX combo or 9
            elif ch == "I" and check_next == "X":
                num = 9
                skip_next = True
            elif ch == "I":
                num = 1
            elif ch == "V":
                num = 5
            elif ch == "X" and check_next == "L":
                num = 40
                skip_next = True
            elif ch == "L":
                num = 50
            elif ch == "X" and check_next == "C":
                num = 90
                skip_next = True
            elif ch == "X":
                num = 10
            elif ch == "C" and check_next == "D":
                num = 400
                skip_next = True
            elif ch == "D":
                num = 500
            elif ch == "C" and check_next == "M":
                num = 900
                skip_next = True
            elif ch == "C":
                num = 100
            elif ch == "M":
                num = 1000
                
            nums.append(num)
            print("nums ea iter", nums)
            
        print("nums", nums)
        total = 0
        for ea in nums:
            total += ea
            
        return total
