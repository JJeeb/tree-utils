def tree(t, 
        children=lambda n: n.get('children', [])):
    yield t
    for c in children(t):
        for e in tree(c) : yield e

