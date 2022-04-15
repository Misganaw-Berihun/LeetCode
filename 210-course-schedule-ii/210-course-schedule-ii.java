class Solution {
    private final int WHITE = 1;
        private final int GREY = 2;
        private final int BLACK = 3;
        
        private Map<Integer, Integer> color;
        private Map<Integer, ArrayList<Integer>> adjList;
        private List<Integer> topologicalOrd;
        private boolean isPossible;
        
        private void init(int numCourses){
            isPossible = true;
            color = new HashMap<>();
            adjList = new HashMap<>();
            topologicalOrd = new ArrayList<>();
            
            for (int i = 0;  i < numCourses; i++){
                color.put(i, WHITE);
            }
        }
    
        private void dfs(int node){
            if (!isPossible){
                return;
            }
            
            color.put(node, GREY);
            for (int neighbour : adjList.getOrDefault(node, new ArrayList<Integer>())){
                if (color.get(neighbour) == WHITE){
                    dfs(neighbour);
                }else if (color.get(neighbour) == GREY){
                    isPossible = false;
                }
            }
            topologicalOrd.add(node);
             color.put(node, BLACK);
        }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        init(numCourses);
    
        for(int[] cor_pre: prerequisites){
            int course = cor_pre[0];
            int pre = cor_pre[1];
            ArrayList<Integer>lst = adjList.getOrDefault(pre, new ArrayList<Integer>());
            lst.add(course);
            adjList.put(pre, lst);
        }
            
        for(int i = 0; i < numCourses; i++){
            if( color.get(i) == WHITE){
                dfs(i);
            }
        }
        
        int [] ord;
        if (isPossible){
            ord = new int[numCourses];
            for(int i = 0; i < numCourses; ++i){
                ord[i] = topologicalOrd.get(numCourses - i - 1);
            }
        }else{
            ord = new int[0];
        }
        
        return ord;
    }
}