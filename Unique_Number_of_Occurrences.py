class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        occurrences = set()
        for count in freq.values():
            if count in occurrences:
                return False
            occurrences.add(count)
        return True

