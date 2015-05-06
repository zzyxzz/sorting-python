##class Solution:
##    # @param s, a string
##    # @return an integer
##    def titleToNumber(self, s):
##        num = 0
##        for i in s:
##            num = num*26 + ord(i)-64
##        return num
##
##sol = Solution()
##s = "AAA"
##print sol.titleToNumber(s)

class Solution:
    # @return a string
    def convertToTitle(self,num):
        ch = ""
        while num > 0:
            mod = (num-1) % 26
            ch += chr(65 + mod)
            num = (num - mod)/26
            print mod,num
        return ch[::-1]

sol = Solution()
s = 52
print sol.convertToTitle(s)

