class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i : 1 for i in range(size)}
        self.res = defaultdict(set)
        
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
        
    def union(self, user1, user2, accounts):
        user1_par = self.find(user1)
        user2_par = self.find(user2)
        
        if self.res.get(user2_par):
            self.res.pop(user2_par)
        if user1_par != user2_par:
            if self.size[user1_par] < self.size[user2_par]:
                user1_par, user2_par = user2_par, user1_par
            self.parent[user2_par] = user1_par
            self.size[user1_par] += self.size[user2_par]
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        user_email = defaultdict(int)
        temp = defaultdict(list)
        res = []
        
        for i in range(n):
            for j in range(1, len(accounts[i])):
                v = accounts[i][j]
                if user_email.get(v) != None and user_email.get(v) != i:
                    uf.union(user_email[v], i, accounts)
                else:
                    user_email[v] = i  
        
        for i in range(n):
            temp[uf.find(i)].append(i)
        
        for k, v in temp.items():
            t = set()
            for val in v:
                t.update(accounts[val][1:])
            res.append([accounts[k][0]] + sorted(t))

        return res