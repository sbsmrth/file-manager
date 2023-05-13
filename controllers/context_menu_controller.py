class MenuController:

    route = ''

    @classmethod
    def open(cls, event, menu, table, path):
        menu.tk_popup(event.x_root, event.y_root)
        item_id = table.identify_row(event.y)  
        item_text = table.item(item_id)['values'][0]  
        item_route = f"{path}{item_text}"
        cls.route = item_route
