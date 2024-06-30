from typing import List

# My Solution
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        pa = [-1]*n
        def find(u, parent) -> int:
            if parent[u] < 0: return u
            parent[u] = find(parent[u], parent)
            return parent[u]
        def union(u, v, parent) -> bool:
            ru = find(u, parent)
            rv = find(v, parent)
            if ru == rv: return False
            if parent[rv] < parent[ru]: ru, rv = rv, ru
            parent[ru] += parent[rv]
            parent[rv] = ru
            return True
        ac = n
        used = 0
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t != 3: continue
            if union(u, v, pa):
                ac -= 1
                used += 1
                if ac == 1: return len(edges)-used
        bc = ac
        pb = pa[:]
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1 and ac > 1 and union(u, v, pa):
                used += 1
                ac -= 1
            if t == 2 and bc > 1 and union(u, v, pb):
                used += 1
                bc -= 1
            if ac == 1 and bc == 1: return len(edges)-used
        return -1

# Best / Most Optimal Solution
class Solution2:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_nodes = [-1] * (n + 1)
        bob_nodes = [-1] * (n + 1)
        def helper_find_parent(family, node):
            if family[node] < 0:
                return node
            family[node] = helper_find_parent(family, family[node])
            return family[node]
        num_redundant_edges = 0
        for typ, u, v in edges:
            if typ == 3:
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)
                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        bob_nodes = alice_nodes.copy()
        for typ, u, v in edges:
            if typ == 1:
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)
                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
            if typ == 2:
                p_u = helper_find_parent(bob_nodes, u)
                p_v = helper_find_parent(bob_nodes, v)
                if p_u != p_v:
                    bob_nodes[p_u] += bob_nodes[p_v]
                    bob_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        al = min(alice_nodes)
        bl = min(bob_nodes)
        if (al == bl and al == -1 * n):
            return num_redundant_edges
        else:
            return -1
