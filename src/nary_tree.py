from src.nary_tree_node import NaryTreeNode

class NaryTree:
    def __init__(self, root):
        self.root = root

    def add_node(self, data, parent=None):
        new_node = NaryTreeNode(data)
        if parent is None:
            self.root = new_node
        else:
            for node in self._find_node(parent, self.root):
                node.children.append(new_node)

    def _find_node(self, data, current_node):
        nodes = []
        if current_node.data == data:
            nodes.append(current_node)
        for child in current_node.children:
            nodes += self._find_node(data, child)
        return nodes

    def find_node(self, data):
        nodes = self._find_node(data, self.root)
        if nodes:
            return nodes[0]
        return None

    def rename_node(self, data, new_data):
        node_find = self.find_node(data)        
        node_find.data = new_data

    def remove_node(self, node_value):
        if self.root is None:
            return  # El árbol está vacío, no hay nada que eliminar

        if self.root.data == node_value:
            self.root = None  # Elimina el nodo raíz
            return

        self._remove_node(self.root, node_value)

    def _remove_node(self, current_node, node_value):
        for child in current_node.children:
            if child.data == node_value:
                current_node.children.remove(child)  # Elimina el nodo hijo
                return

            self._remove_node(child, node_value)  # Recursivamente busca en los hijos

