import csv

characteristics_file = "characteristics_xpath.csv"


class BookParsePattern:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.book_name_xpath = ""
        self.book_characteristics = []

    def read_csv_with_characteristics(self):
        with open(self.file_path, "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row_number, row in enumerate(csv_reader):
                key, value = row
                if row_number == 0:
                    self.book_name_xpath = value
                else:
                    self.book_characteristics.append((key, value))


def get_book_settings(path: str) -> BookParsePattern:
    book = BookParsePattern(path)
    book.read_csv_with_characteristics()
    return book


book_xpath = get_book_settings(characteristics_file)
