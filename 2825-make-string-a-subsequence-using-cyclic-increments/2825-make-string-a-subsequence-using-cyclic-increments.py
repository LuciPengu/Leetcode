class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for c in str1:
            if i == len(str2):
                return True
            
            
            upOne = chr(ord(c)+1) if c != 'z' else 'a'
            if str2[i] == c or upOne == str2[i]:
                i += 1
        return i == len(str2)