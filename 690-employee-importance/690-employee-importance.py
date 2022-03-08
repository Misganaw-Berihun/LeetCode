"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.count=0
        self.visited = set()
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp):
            self.visited.add(emp.id)
            self.count += emp.importance
            
            for sub in emp.subordinates:
                if sub in self.visited:
                    continue
                    
                for e in employees:
                    if e.id == sub:
                        dfs(e)
                                   
        emp = None
        
        for e in employees:
            if e.id == id:
                emp = e
                
        dfs(emp)
        return self.count
                    
                    
        