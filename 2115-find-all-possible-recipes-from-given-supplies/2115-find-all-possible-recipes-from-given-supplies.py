class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipies = set(recipes)
        ans = []
        adjacency_list = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque(supplies)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingre in ingredients[i]:
                adjacency_list[ingre].append(recipe)
                indegree[recipe] += 1
                
        while queue:
            cur = queue.popleft()
            if cur in recipies:
                ans.append(cur)
            
            for nei in adjacency_list[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return ans
                
        
                
        
        