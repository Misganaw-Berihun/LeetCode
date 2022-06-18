class Solution {
    private static int [] dfs(Map<Integer, List<Integer>> adjList, int cur, String labels, int [] result, Set<Integer> visited){
        visited.add(cur);
        
        if (!adjList.containsKey(cur)){
            int [] arr = new int[26];
            Arrays.fill(arr, 0);
            result[cur] = ++arr[labels.charAt(cur) - 'a'];
            return arr;
        }
        int [] temp = new int[26];
        for (int edge : adjList.get(cur)){
            if (visited.contains(edge)) continue;
            int [] ret = dfs(adjList, edge, labels, result, visited);
            for (int i = 0; i < 26; i++){
                temp[i] += ret[i];
            }
        }
        result[cur] = ++temp[labels.charAt(cur) - 'a'];
        return temp;
    }
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        Map<Integer, List<Integer>> adjList = new HashMap<Integer, List<Integer>>();
        Set<Integer> visited = new HashSet<Integer>();
        int [] result = new int[n];
        
        for (int [] edge : edges){
            List<Integer> temp1 = adjList.getOrDefault(edge[0], new ArrayList<Integer>());
            List<Integer> temp2 = adjList.getOrDefault(edge[1], new ArrayList<Integer>());
            temp1.add(edge[1]);
            temp2.add(edge[0]);
            adjList.put(edge[0], temp1);
            adjList.put(edge[1], temp2);
        }
        
        dfs(adjList, 0, labels, result, visited);
        return result;
    }
}