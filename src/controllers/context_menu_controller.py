class MenuController:
    """
    Controlador para el menú contextual de la aplicación.
    """
    route = ''
    id = ''

    @classmethod
    def open(cls, event, menu, table, path):
        """
        Abre el menú contextual en respuesta a un evento de clic derecho en la tabla.
        Obtiene la información del elemento seleccionado en la tabla.

        Parámetros:
        -----------
        event : tkinter.Event
            El evento que desencadenó la apertura del menú contextual.
        menu : tkinter.Menu
            El menú contextual que se va a abrir.
        table : tkinter.ttk.Treeview
            La tabla Treeview asociada al menú contextual.
        path : str
            La ruta actual del elemento al que se le dio clic derecho.
        """
        menu.tk_popup(event.x_root, event.y_root)  # Muestra el menú contextual en las coordenadas especificadas.
        cls.id = table.identify_row(event.y)  # Actualiza el atributo de clase 'id' al obtener el ID del elemento seleccionado de la tabla.
        item_text = table.item(cls.id)['values'][0]  # Obtiene el primer valor del elemento seleccionado de la lista de valores.
        item_route = f"{path}/{item_text}"  # Concatena la variable 'path' (ruta) con la variable 'item_text' (texto del elemento seleccionado).
        cls.route = item_route  # Actualiza el atributo de clase 'route'. #concatenar la variable path (ruta) con la variable item_text (texto del elemento seleccionado)
