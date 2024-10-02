def createGraph(chars: list[str], edges: list[tuple[int]]) -> dict:
    tree = {}
    
    for (start, end) in edges:
        if start not in tree:
            tree[start] = []
        if end not in tree:
            tree[end] = []
        tree[end].append(start)
        tree[start].append(end)    
    return tree

def solution(tree: dict, rules: list[tuple], char: list[str]) -> str:
    
    m = {}
    for (index, value) in enumerate(chars):
        m[index] = value
    
    output = ""
    for rule in rules:
        
        s = dfs(tree, rule, m)
        print(s)
        if is_palindrome(s):
            output += "YES\n"
        else:
            output += "NO\n"
    return output

def is_palindrome(s: str) -> bool:
    return s == s[::-1] 

def dfs(tree: dict, rule: tuple, char_map: dict) -> str:
    root, leaf = rule
    return dfs_rec(tree, root, leaf, char_map)

def dfs_rec(tree, root, leaf, char_map, visited=None):
    if visited is None:
        visited = set()
    visited.add(root)

    if root == leaf:
        return char_map[root]
    
    
    for neigh in tree[root]:
        if neigh not in visited:
            path = dfs_rec(tree, neigh, leaf, char_map, visited)
            if path:
    
                return char_map[root] + path
    
    return ""


chars = ["b", "c", "b"]
tree = createGraph(chars, [(0, 1), (1, 2)])
string = solution(tree, [(0, 2), (0, 5)], chars)
print(string)