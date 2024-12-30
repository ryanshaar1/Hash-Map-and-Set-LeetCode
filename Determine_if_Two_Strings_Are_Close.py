class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!= len(word2):
            return False
        freq1 = {}
        for char in word1:
            freq1[char] = freq1.get(char,0)+1
        freq2 = {}
        for char in word2:
            freq2[char] = freq2.get(char,0)+1
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        return True