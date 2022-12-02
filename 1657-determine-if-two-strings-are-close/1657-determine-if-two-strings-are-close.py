class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        count3 = defaultdict(int)
        
        for i in count1.keys():
            count3[count1[i]] += 1
        
        close = True
        for i in count2.keys():
            key = count2[i]
            if count3[key] <= 0 or i not in count1:
                close = False
            count3[key] -= 1
        
        return close