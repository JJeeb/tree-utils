def iter_tree(tree,
        children=lambda n: n.get('children', [])):
    yield tree
    for c in children(tree):
        for e in iter_tree(c):
             yield e

def enumerate_paths(tree,
        children=lambda n: n.get('children', []),
        name=lambda n: n['name'],
        path=None):
    path = path or [name(tree)]
    yield (path, tree)
    for c in children(tree):
        new_path = path + [name(c)]
        for enum in enumerate_paths(c, path=new_path):
             yield enum 

def find_by_path(t, search_path):
    return next((node for path, node in enumerate_paths(t) if path == search_path), None)

def from_path_list(path_list):
    paths = (path_from_string(p) for p in path_list)
    return reduce(insert, paths, {})

def insert(tree, path):
    if not path: return tree
    head, tail = path[0], path[1:]
    if not tree: return insert({'name' : head}, tail)
    if tree['name'] == head: 
       insert(tree, tail)    
       return tree
    for c in tree.get('children', []):
        if c['name'] == head:
            insert(c, tail)
            return tree
    tree.setdefault('children', []).append(insert({'name': head}, tail))
    return tree 

def child(tree, name):
    child = find_child_by_name(tree, name)
    if not child:
        child = {'name': name}
        tree.setdefault('children', []).append(child)
    return child

def find_child_by_name(tree, name):
    return next((e for e in tree.get('children', []) if e['name'] == name), None)

def path_from_string(path):
    if not path.startswith('/'): raise ValueError
    return path.split('/')[1:]
