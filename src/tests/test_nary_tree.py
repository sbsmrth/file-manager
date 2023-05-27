from src.nary_tree import NaryTree
from src.nary_tree_node import NaryTreeNode
import pytest

@pytest.fixture
def tree():
    instance = NaryTree(NaryTreeNode('C://'))
    return instance

@pytest.mark.parametrize(
    "data, new_data",
    [
        ('old.txt', 'new.txt'),
        (['write.txt', 'read.txt'])
    ]
)

def test_rename_node(tree, data, new_data):
    tree.add_node(data, tree.root.data)
    node = tree.find_node(data)
    tree.rename_node(data, new_data)
    assert node.data == new_data
    assert tree.find_node(data) is None

def test_add_node(tree):
    path = f"{tree.root.data}exm.exe"

    prev_length = len(tree.root.children)
    tree.add_node(path, tree.root.data)

    assert len(tree.root.children) == prev_length + 1
    assert tree.root.children[0].data == path

def test_find_node(tree):
    path = f"{tree.root.data}exm.exe"
    tree.add_node(path, tree.root.data)
    node = tree.find_node(path)
    
    assert node is not None
    assert node.data == path

@pytest.mark.parametrize(
    "children, expected",
    [
        (['text.txt', 'some.txt', 'last.png'], 2),
        (['text.txt', 'some.html'], 1)
    ]
)

def test_remove_node(tree, children, expected):
    [tree.add_node(f"{tree.root.data}{child}", tree.root.data) for child in children]
    tree.remove_node(tree.root.children[0].data)

    assert len(tree.root.children) == expected
