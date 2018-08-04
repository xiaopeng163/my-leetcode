class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i].lower() not in vowels and (i < j):
                i += 1
            while s[j].lower() not in vowels and (i < j):
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
