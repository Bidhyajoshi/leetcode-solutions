class Solution(object):
    def removeOuterParentheses(self, s):

        result = ""
        count = 0

        for char in s:

            if char == '(':
                if count > 0:
                    result += char
                count += 1

            else:
                count -= 1
                if count > 0:
                    result += char

        return result