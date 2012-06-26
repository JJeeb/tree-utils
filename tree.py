def tree(t, 
        children=lambda n: n.get('children', [])):
    yield t
    for c in children(t):
        for e in tree(c):
             yield e

def enumerate_paths(t,
        children=lambda n: n.get('children', []),
        name=lambda n: n['name'],
        path=None):
    path = path or [name(t)]
    yield (path, t)
    for c in children(t):
        new_path = path + [name(c)]
        for enum in enumerate_paths(c, path=new_path):
             yield enum 

def find_by_path(t, search_path):
    return next((node for path, node in enumerate_paths(t) if path == search_path), None)

