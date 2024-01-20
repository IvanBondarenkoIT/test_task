import csv
from task_2.parser.interaction import BookScraper

RESULT_CSV_FILE_PATH = "books.csv"


def get_csv(link: str):
    print(f"START PARSING {link}")

    scraper = BookScraper(
        link
        # "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        # "https://books.toscrape.com/catalogue/category/books/politics_48/index.html"
    )
    scraper.scrape_books()
    scraper.close_driver()
    scraper.save_to_csv(RESULT_CSV_FILE_PATH)
    return RESULT_CSV_FILE_PATH
