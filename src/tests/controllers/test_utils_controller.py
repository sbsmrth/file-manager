import pytest
from src.nary_tree import NaryTree
from src.nary_tree_node import NaryTreeNode
from src.controllers.utils_controller import UtilsController

@pytest.fixture
def tree():
    instance = NaryTree(NaryTreeNode('C://'))
    return instance

@pytest.mark.parametrize(
    "children, current, new_dest",
    [
        (['Riot Games', 'random.py', 'newDestiny'], 1, 2)
    ]
)

def test_copy_and_paste(tree, children, current, new_dest):
    [tree.add_node(f"{tree.root.data}{child}", tree.root.data) for child in children]

    current_path = f"{tree.root.data}{children[current]}"
    new_dest_path = f"{tree.root.data}{children[new_dest]}"
    assert tree.find_node(new_dest) is None
    assert tree.find_node(current_path) is not None
    UtilsController.copy_and_paste(current_path, tree, new_dest_path)
    assert tree.find_node(new_dest_path) is not None
    assert tree.find_node(current_path) is not None