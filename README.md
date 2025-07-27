Королёв Владислав 4 спринт.
Тестирование приложения BooksCollector:
-- Тесты add_new_book

- test_add_new_book_adds_book — проверяет, что книга успешно добавляется в коллекцию.
- test_add_new_book_long_name_is_ignored — проверяет, что книга с названием длиной более 40 символов не добавляется.

-- Тест set_book_genre

- test_set_book_genre_sets_genre_correctly — проверяет корректное присвоение жанра существующей книге.

-- Тест get_book_genre

- test_get_book_genre_returns_correct_genre — параметризованный тест, проверяющий, что метод возвращает правильный жанр книги.

-- Тесты get_books_with_specific_genre

- test_get_books_with_specific_genre_returns_books — параметризованный позитивный тест, проверяющий, что возвращаются книги с указанным жанром.
- test_get_books_with_specific_genre_returns_empty_list_for_unknown_genre — проверка, что для неизвестного жанра возвращается пустой список.

-- Тест get_books_genre

- test_get_books_genre_returns_correct_dict — проверяет, что метод возвращает полный словарь книг с жанрами.