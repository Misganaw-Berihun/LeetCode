class Unionfind:
    def __init__(self):
        self.parent = {chr(i): chr(i) for i in range(97, 123)}
        
    def find(self, char):
        if self.parent[char] != char:
            self.parent[char] = self.find(self.parent[char])
        return self.parent[char]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        
        if a != b:
            if a > b:
                a, b = b, a
                
            self.parent[b] = a
            
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = Unionfind()
        len_word = len(s1)
        len_parser = len(baseStr)
        equivalent = []
        
        for i in range(len_word):
            uf.union(s1[i], s2[i])
        
        for i in range(len_parser):
            ch = baseStr[i]
            smallest = uf.find(ch)
            equivalent.append(smallest)
        
        return ''.join(equivalent)
            
        