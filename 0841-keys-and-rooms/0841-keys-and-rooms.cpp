class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int> visited;
        queue<int> q;
        visited.insert(0);
        q.push(0);
        
        while (q.size() > 0){
            int cur = q.front();
            q.pop();
            
            for (int i = 0; i < rooms[cur].size(); i++){
                int new_node = rooms[cur][i];
                
                if (visited.find(new_node) == visited.end()){
                    q.push(new_node);
                    visited.insert(new_node);
                }
            }
        }
        return rooms.size() == visited.size();
    }
};