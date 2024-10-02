def solution(cp, cm, edges):
    root = edges[0][0]  
    
    tree = {}
    for (start, end) in edges:
        if start not in tree:
            tree[start] = set()
        if end not in tree:
            tree[end] = set()
        tree[start].add(end)
    
    print(tree)
    
    archi_tolti, visited = dfs(cp, cm, tree, root)
    costo_archi_tolti = archi_tolti * cm
    costo_archi_aggiunti = 0
    
    for node in tree.keys():
        if node not in visited:
            archi_tolti, visited = dfs(cp, cm, tree, node, visited)
            tree[root].add(node)
            costo_archi_aggiunti += cp
    
    costo_archi_tolti += archi_tolti * cm
    
    return costo_archi_tolti + costo_archi_aggiunti, tree
    
def dfs(cp, cm, tree, root, visited=None):
    if visited is None:
        visited = set()
    
    archi_tolti = 0
    visited.add(root)
    
    for neigh in list(tree[root]):
        if neigh not in visited:
            a, _  = dfs(cp, cm, tree, neigh, visited)
            archi_tolti += a
        else:
            tree[root].remove(neigh)
            archi_tolti += 1
    
    return archi_tolti, visited
    
x, tree = solution(10, 10, [(1, 2), (1, 3), (1, 4)])
print(x)
print(tree)