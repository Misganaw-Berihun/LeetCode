/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    List<Integer> preorder = new ArrayList<Integer>();
    private  void dfs(Node rt){
        if (rt == null){
            return;
        }
        preorder.add(rt.val);
        for(Node child : rt.children){
            dfs(child);
        }
    }
    public List<Integer> preorder(Node root) {
        dfs(root);
        return preorder;
    }
}