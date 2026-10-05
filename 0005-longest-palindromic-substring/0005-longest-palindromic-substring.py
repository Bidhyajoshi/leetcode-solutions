class Solution(object):
    def longestPalindrome(self, s):
      start=0
      maxlength=1

      def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right-left-1  #to find length of palindromic substring

      for i in range(len(s)):
        len1= expand(i,i)
        len2= expand(i,i+1)

        length = max(len1,len2)

        if length> maxlength:
           maxlength = length
           start = i-(length-1)//2

      return s[start:start+ maxlength]       


