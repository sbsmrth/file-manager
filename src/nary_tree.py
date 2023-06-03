from src.nary_tree_node import NaryTreeNode

class NaryTree:
    def __init__(self, root):
        self.root = root

    def add_node(self, data, parent = None):
        """
        metodo que permite agregar un nuevo nodo al arbol

        parametros
        ------------
        data: str
            valor del nodo que se quiere agregar
        parent: nodo or None
            valor del nodo padre al que se quiere añadir
        """
        new_node = NaryTreeNode(data)
        if parent is None:
            self.root = new_node
        else:
            for node in self._find_node(parent, self.root):
                node.children.append(new_node)

    def _find_node(self, data, current_node):
        """
            metodo priavado para buscar un nodo en el arbol

            parametros
            -----------
            data: str
               valor del nodo que se quiere buscar
            current_node: NaryTreeNode
                valor del nodo, desde donde se quiere iniciar la busqueda

            returns
            -----------
            list:
                lista de nodos que coincide con el valor buscado
        """
        nodes = []  # Lista para almacenar los nodos encontrados.

        if current_node.data == data:  # Si el valor del nodo actual coincide con el valor buscado...
            nodes.append(current_node)  # Agregar el nodo actual a la lista de nodos encontrados.

        for child in current_node.children:  # Para cada hijo del nodo actual.
            nodes += self._find_node(data, child)  # Realizar una búsqueda recursiva llamando al método _find_node con el hijo como nuevo nodo actual y agregar los nodos encontrados a la lista.

        return nodes  # Retornar la lista de nodos encontrados.

    def find_node(self, data):
        """
            metodo publico que permite encontrar un nodo especifico

            parameters
            -----------
            data: str
                el valor del nodo que se quiere encontrar

            returns
            ------------
            node or None:
                el nodo buscado o None en caso de no encontrarlo

        """
        nodes = self._find_node(data, self.root) #llama al metodo privado para encontrar el nodo
        if nodes:
            return nodes[0]
        return None

    def rename_node(self, data, new_data):
        """
            permite cambiar el nombre de un nodo.
            
            parameters
            ------------
            data: str
                corresponde al nodo que se le asignara un nuevo nombre.
            new_Data : str
                corresponde al nuevo nombre del nodo.
        """
        node_find = self.find_node(data)        
        node_find.data = new_data

    def remove_node(self, node_value):
        """
        metodo publico que permite eliminar un nodo del arbol

        parametros
        ------------
        node_value: NaryTreeNode
            el valor del nodo que se desea eliminar

        returns
        ------------
            None
        """
        if self.root is None:
            return  # El árbol está vacío, no hay nada que eliminar

        if self.root.data == node_value:
            self.root = None  # Elimina el nodo raíz
            return

        self._remove_node(self.root, node_value)

    def _remove_node(self, current_node, node_value):
        """
        metodo privado que permite eliminar un nodo del arbol

        parametros
        ------------
        current_node: NaryTreeNode
            El nodo actual desde donde se iniciará la búsqueda de los hijos.
        node_value: NaryTreeNode
            valor del nodo que se quiere eliminar

        returns
        ------------
        None
        """
        for child in current_node.children:
            if child.data == node_value:
                current_node.children.remove(child)  # Elimina el nodo hijo
                return

            self._remove_node(child, node_value)  # Recursivamente busca en los hijos

