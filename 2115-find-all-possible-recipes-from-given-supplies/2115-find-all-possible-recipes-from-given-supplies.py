class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipies = set(recipes)
        ans = []
        adjacency_list = defaultdict(list)
        indegree = {recipes[i] : 0 for i in range(len(recipes))}
        queue = deque()
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingre in ingredients[i]:
                adjacency_list[ingre].append(recipe)
                indegree[recipe] += 1
        
        for sup in supplies:
            queue.append(sup)
            
        while queue:
            cur = queue.popleft()
            if cur in recipies:
                ans.append(cur)
            
            for nei in adjacency_list[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return ans
                
        
                
        
        