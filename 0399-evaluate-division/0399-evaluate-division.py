from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list  = defaultdict(list)

        for i, eq in enumerate(equations):
            numo, deno = eq
            adj_list[numo].append([deno, values[i]])
            adj_list[deno].append([numo, 1 / values[i]])

        def bfs_helper(src, target):
            if src not in adj_list or target not in adj_list:
                return -1

            q = deque()
            visited = set()

            q.append([src, 1])
            visited.add(src)

            while q:
                initial_node, initial_weight = q.popleft()
                if initial_node == target:
                    return initial_weight

                for neighbor_node, neighbor_weight in adj_list[initial_node]:
                    if neighbor_node not in visited:
                        q.append([neighbor_node, initial_weight * neighbor_weight])
                        visited.add(neighbor_node)

            return -1


        return [bfs_helper(q[0], q[1]) for q in queries]
        