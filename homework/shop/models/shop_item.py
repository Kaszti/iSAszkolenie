import openpyxl as xl


class Item():
    def __init__(self, item_id, name,create_date, last_buy_date, amount_available):
        self.id: int = item_id
        self.name: str = name
        self.create_date = create_date
        self.last_buy_date = last_buy_date
        self.amount_available: int = amount_available
    item_type: str = None