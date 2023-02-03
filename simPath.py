class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = []
        cur_part = ''

        for char in path + '/':
            if char == '/':
                if cur_part == '..':
                    if parts:
                        parts.pop()
                elif cur_part and cur_part != '.':
                    parts.append(cur_part)
                cur_part = ''
            else:
                cur_part += char

        return '/' + '/'.join(parts)
