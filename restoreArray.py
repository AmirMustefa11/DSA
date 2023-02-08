class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        connections = {}
        for i, j in adjacentPairs:
            connections[i] = connections.get(i, []) + [j]
            connections[j] = connections.get(j, []) + [i]

        start = next(iter(connections))
        for node in connections:
            if len(connections[node]) == 1:
                start = node
                break

        result = []
        visited = set()
        self.dfs(start, result, visited, connections)
        return result

    def dfs(self, node, result, visited, connections):
        result.append(node)
        visited.add(node)
        for connected_node in connections[node]:
            if connected_node not in visited:
                visited.add(connected_node)
                self.dfs(connected_node, result, visited, connections)
