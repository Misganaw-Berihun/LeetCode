class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites)
    {
            Queue<Integer>  queue = new LinkedList<Integer>();
            int [] indegree = new int[numCourses];
            Map<Integer, ArrayList<Integer>> edges = new HashMap<>();
            ArrayList<Integer> topSort = new ArrayList<>();
            
            for(int i = 0; i < prerequisites.length; ++i)
            {
                    ArrayList<Integer> temp = edges.getOrDefault(prerequisites[i][1], new ArrayList<Integer>());
                    temp.add(prerequisites[i][0]);
                    edges.put(prerequisites[i][1], temp);
                    indegree[prerequisites[i][0]] += 1;
            }
            for (int i = 0; i < numCourses; ++i)
            {
                    if (indegree[i] == 0)
                    {
                            queue.add(i);
                    }
            }
            
            while (queue.size() != 0)
            {
                    int cur = queue.remove();
                    topSort.add(cur);
                    for (int course: edges.getOrDefault(cur, new ArrayList<>()))
                    {
                            indegree[course]--;
                            if (indegree[course] == 0)
                            {
                                    queue.add(course);
                            }
                    }
            }   
            return topSort.size() == numCourses;    
    }
}