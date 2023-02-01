class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = 0
        index = 0
        while index < len(blocks) - k + 1:
            current_block = blocks[index: index + k]
            if index == 0:
                min_ops += current_block.count("W")
            else:
                min_ops = min(min_ops, current_block.count("W"))
            index += 1

        return min_ops
