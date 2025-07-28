import pytest
from main import BooksCollector
class TestBooksCollector:

 def test_add_new_book_adds_book():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.books_genre

@pytest.mark.parametrize("long_name", [
    "а" * 41,
    "д" * 50,
    "книга" * 10,
])
def test_add_new_book_long_name_is_ignored(long_name):
    collector = BooksCollector()
    collector.add_new_book(long_name)
    assert long_name not in collector.books_genre

def test_set_book_genre_sets_genre_correctly():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.books_genre["Гарри Поттер"] == "Фантастика"

@pytest.mark.parametrize("book, genre", [
    ("Гарри Поттер", "Фантастика"),
    ("Война и мир", "Роман"),
    ("Звездные войны", "Фантастика"),
])
def test_get_book_genre_returns_correct_genre(book, genre):
    collector = BooksCollector()
    collector.books_genre = {book: genre}
    assert collector.get_book_genre(book) == genre

@pytest.mark.parametrize("genre, expected_books", [
    ("Фэнтези", ["Книга 3", "Книга 2"]),
    ("Роман", ["Книга 1"]),
])
def test_get_books_with_specific_genre_returns_books(genre, expected_books):
    collector = BooksCollector()
    collector.books_genre = {
        "Книга 3": "Фэнтези",
        "Книга 1": "Роман",
        "Книга 2": "Фэнтези"
    }
    books = collector.get_books_with_specific_genre(genre)
    assert sorted(books) == sorted(expected_books)

def test_get_books_with_specific_genre_returns_empty_list_for_unknown_genre():
    collector = BooksCollector()
    collector.books_genre = {"Книга 3": "Фэнтези"}
    empty_list = collector.get_books_with_specific_genre("Неизвестный жанр")
    assert empty_list == []

def test_get_books_genre_returns_correct_dict():
    collector = BooksCollector()
    collector.books_genre = {
        "Книга 1": "Драма",
        "Книга 2": "Фантастика"
    }
    genres = collector.get_books_genre()
    assert genres == {
        "Книга 1": "Драма",
        "Книга 2": "Фантастика"
    }