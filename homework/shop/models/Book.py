import homework.shop.models.shop_item as item

class Book(item.Item):
    def __init__(self, item_id, name, create_date, last_buy_date, amount_available, author, number_of_pages):
        super().__init__(item_id, name, create_date, last_buy_date, amount_available)
        self.author = author
        self.number_of_pages = number_of_pages
    item_type: str = 'Book'
