from stats import convert_text
from stats import get_book_text
from stats import text_converter

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = convert_text(book_text)
    print(f"{words} words found in the document")
    print(f"{text_converter(book_text)}")
    

main()

