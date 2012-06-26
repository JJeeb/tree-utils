from tree import tree
from nose.tools import assert_equal

TECHNOLOGIES = { 
    'name': 'Technology',
    'children': [
        {'name': 'Programming',
        'children': [ {'name': 'Python'}, {'name': 'Ruby'}]},
        {'name': 'Enterprise',
         'children': [ {'name': 'Mac'}, {'name': 'Mobile'}]}]
    }


def test_iter_tree():
    assert_equal([{'children': [{'children': [{'name': 'Python'}, {'name': 'Ruby'}],
                   'name': 'Programming'},
                  {'children': [{'name': 'Mac'}, {'name': 'Mobile'}],
                   'name': 'Enterprise'}],
                 'name': 'Technology'},
            {'children': [{'name': 'Python'}, {'name': 'Ruby'}], 'name': 'Programming'},
            {'name': 'Python'},
            {'name': 'Ruby'},
            {'children': [{'name': 'Mac'}, {'name': 'Mobile'}], 'name': 'Enterprise'},
            {'name': 'Mac'},
            {'name': 'Mobile'}],
    list(tree(TECHNOLOGIES)))

def is_leaf(e):
    return 'children' not in e

def test_generator_expression():
    assert_equal(['Technology', 'Programming', 'Python', 'Ruby', 
                'Enterprise', 'Mac', 'Mobile'], 
        list(e['name'] for e in tree(TECHNOLOGIES)))

    assert_equal(['Python', 'Ruby', 'Mac', 'Mobile'], 
        list(e['name'] for e in tree(TECHNOLOGIES) if is_leaf(e)))

def test_update_with_side_effect():
    technologies = { 
        'name': 'Technology',
        'children': [
        {
            'name': 'Programming',
            'children': [
            {'name': 'Python'},
            {'name': 'Ruby'}
            ]
        }]} 
    
    python = (e for e in tree(technologies) if e['name'] == 'Python').next()
    python.update(tag='cool')

    assert_equal({ 
        'name': 'Technology',
        'children': [
        {
            'name': 'Programming',
            'children': [
            {'name': 'Python', 'tag': 'cool'},
            {'name': 'Ruby'}
            ] }]}, 
    technologies) 
    
