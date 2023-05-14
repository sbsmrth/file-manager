class MenuController:

    route = ''
    id = ''

    @classmethod
    def open(cls, event, menu, table, path):
        menu.tk_popup(event.x_root, event.y_root)
        cls.id = table.identify_row(event.y)
        item_text = table.item(cls.id)['values'][0]  
        item_route = f"{path}{item_text}"
        cls.route = item_route
