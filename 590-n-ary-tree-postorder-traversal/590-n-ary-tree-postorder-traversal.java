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
     public List<Integer> postorder(Node root) {
         if (root == null) return new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        Stack<Node> stk = new Stack<>();
         stk.push(root);
         
         while (!stk.empty()){
             Node cur = stk.pop();
             for (Node child: cur.children){
                 stk.push(child);
             }
             result.add(cur.val);
         }
        Collections.reverse(result);
         return result;
    }
}