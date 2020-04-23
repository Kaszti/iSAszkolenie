import homework.shop.models.Book as book

class Ebook(book.Book):
    def __init__(self, item_id, name, create_date, last_buy_date, amount_available, author, number_of_pages, file_format):
        super().__init__(item_id, name, create_date, last_buy_date, amount_available, author, number_of_pages)
        self.file_format: str = file_format
    item_type: str = 'Ebook'