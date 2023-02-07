class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if './' == log:
                continue
            elif '..' in log:
                count = max(0, count-1)
            else:
                count += 1

        return count
