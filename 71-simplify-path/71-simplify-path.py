class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split('/')
        stk = []
        for p in temp:
            if p == "" or p == '.':
                continue
            if p == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(p)
        return '/' + '/'.join(stk)
            