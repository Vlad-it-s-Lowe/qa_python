import pytest
from main import BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "Властелин колец",
        "Гарри Поттер и философский камень",
        "Дюна"
    ])
    def test_add_new_book_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert book_name in books
        assert books[book_name] == ''

    def test_add_new_book_fail_long_name(self):
        collector = BooksCollector()
        long_name = "а" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        book_name = "Дюна"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert list(books.keys()).count(book_name) == 1

    def test_set_book_genre_valid_and_invalid(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

        collector.set_book_genre("Гарри Поттер", "Неизвестный жанр")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Фантастика")

        books_fantasy = collector.get_books_with_specific_genre("Фантастика")
        assert "Книга1" in books_fantasy
        assert "Книга3" in books_fantasy
        assert "Книга2" not in books_fantasy

        empty_list = collector.get_books_with_specific_genre("Неизвестный жанр")
        assert empty_list == []

    def test_get_books_for_children_no_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")

        collector.add_new_book("Страшилка")
        collector.set_book_genre("Страшилка", "Ужасы")

        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books
        assert "Страшилка" not in children_books

    def test_add_book_in_favorites_uniqueness(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")

        collector.add_book_in_favorites("Любимая книга")
        favorites = collector.get_list_of_favorites_books()
        assert "Любимая книга" in favorites

        collector.add_book_in_favorites("Любимая книга")
        assert favorites.count("Любимая книга") == 1

        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")

        collector.delete_book_from_favorites("Любимая книга")
        favorites = collector.get_list_of_favorites_books()
        assert "Любимая книга" not in favorites

        collector.delete_book_from_favorites("Несуществующая книга")
        assert isinstance(collector.get_list_of_favorites_books(), list)

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []