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
    if not tree: return insert(create_node(name=head), tail)
    if tree['name'] == head: return insert(tree, tail)    
    for c in tree.get('children', []):
        if c['name'] == head:
            return insert(c, tail)
    tree.setdefault('children', []).append(insert(create_node(name=head), tail))
    return tree 

def create_node(name):
    return {'name': name}

def path_from_string(path):
    if not path.startswith('/'): raise ValueError
    return path.split('/')[1:]
