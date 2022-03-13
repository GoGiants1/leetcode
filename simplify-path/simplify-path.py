class Solution:
    def simplifyPath(self, path: str) -> str:
        CURR = "."
        UP = ".."

        n = len(path)
        p_list = path.split('/')
        can_path = []
        for i, v in enumerate(p_list):
            if v == CURR:
                continue
            elif v == UP:
                if can_path:
                    can_path.pop()
            elif v != '':
                can_path.append(v)
                
        return '/'+'/'.join(can_path)