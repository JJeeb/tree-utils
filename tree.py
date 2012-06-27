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

