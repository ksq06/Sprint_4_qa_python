import pytest

from main import BooksCollector
from test.data import BOOKS

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize("book", ["", "А" * 41])
    def test_add_new_book_invalid_length(self, books_collector, book):
        books_collector.add_new_book(book)
        assert book not in books_collector.get_books_genre()

    def test_new_book_has_no_genre(self, books_collector):
        books_collector.add_new_book("Новая книга")
        assert books_collector.get_book_genre("Новая книга") == ""

    def test_add_new_book_duplicate(self, books_collector):
        books_collector.add_new_book('Незнайка на Луне')

        books_collector.add_new_book('Незнайка на Луне')

        assert len(books_collector.get_books_genre()) == 1
        assert 'Незнайка на Луне' in books_collector.get_books_genre()

    def test_books_genre_fav_dict_is_empty(self, books_collector):
        assert books_collector.books_genre == {}
        assert books_collector.favorites == []

    def test_genre_list_is_not_empty(self, books_collector):
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector):
        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize("name, data", BOOKS)
    def test_add_book_with_genre_and_rating(self, books_collector, name, data):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, data["genre"])

        assert books_collector.get_book_genre(name) == data["genre"]


    @pytest.mark.parametrize("name, data", BOOKS)
    def test_get_books_for_children_correct_genre(self, books_collector, name, data):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, data["genre"])

        children_books = books_collector.get_books_for_children()
        is_adult_genre = data["genre"] in books_collector.genre_age_rating

        assert (name not in children_books) == is_adult_genre

    @pytest.mark.parametrize("name, data", BOOKS)
    def test_get_books_for_children_adult_rating(self, books_collector, name, data):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, data["genre"])

        assert (name not in books_collector.get_books_for_children()) == (data["genre"] in books_collector.genre_age_rating)

    def test_get_books_for_children_for_children(self, books_collector):
        books_collector.add_new_book("Малыш и Карлсон")
        books_collector.set_book_genre("Малыш и Карлсон", "Мультфильмы")

        books_for_children = books_collector.get_books_for_children()
        assert "Малыш и Карлсон" in books_for_children

    @pytest.mark.parametrize("name", [BOOKS[0][0]])
    def test_add_book_in_favorites_when_books_in_list(self, books_collector, name):
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)

        assert name in books_collector.favorites

    @pytest.mark.parametrize("book", ["Несуществующая книга"])
    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector, book):
        assert not books_collector.add_book_in_favorites(book)

    @pytest.mark.parametrize("name", [BOOKS[1][0]])
    def test_delete_book_from_favorites(self, books_collector, name):
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)

        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.favorites

    @pytest.mark.parametrize("book", ["Несуществующая книга"])
    def test_delete_book_from_favorites_no_name_in_list(self, books_collector, book):
        assert not books_collector.delete_book_from_favorites(book)

    def test_get_list_of_favorites_books_not_empty(self, books_collector):
        for name, _ in BOOKS[:3]:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self, books_collector):
        name = BOOKS[4][0]
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)

        assert not books_collector.get_list_of_favorites_books()