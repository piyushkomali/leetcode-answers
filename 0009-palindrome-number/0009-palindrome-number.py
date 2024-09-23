#objective: see if an integer is read the same forwards and backwards

# immediate check -> if number is negative it is always false since if you flip it a negative at the end is invalid
# in order to check for equivalencies and iterate through each digit we need to convert to string using str() funct
# using 2 pointer method we declare 2 pointers to front and back of string
# we use while loop that ends only when the 2 pointers meet in the middle[odd #] or pass each other[even #] 
#                 startPointer --->  <--- endPointer
# if at any point the string values of the pointer do not equal each other we return False(0) since it would not be a palidrome
# otherwise increment pointers, once it finishes the while loop we know it is True so we return True(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        string = str(x)
        pointerStart = 0
        pointerEnd = len(string) - 1
        while (pointerStart <= pointerEnd):
            if(string[pointerStart] !=  string[pointerEnd]):
                return False
            else:
                pointerStart += 1
                pointerEnd -= 1
        return 1
