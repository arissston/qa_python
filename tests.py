import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name,genre', [
        ('Гордость и предубеждение и зомби', 'Комедии'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы')])
    def test_set_book_genre_genre_successfully_set(self, collector_with_books,
                                                   book_name, genre):
        collector_with_books.set_book_genre(book_name, genre)

        assert collector_with_books.get_book_genre(book_name) == genre

    def test_get_book_genre_genre_is_shown_correctly(self, collector_with_books):
        assert collector_with_books.get_book_genre(
            'Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_books_with_specific_genre_show_books_from_genre(self, collector_with_books):
        assert 'Что делать, если ваш кот хочет вас убить' in collector_with_books.get_books_with_specific_genre(
            'Ужасы')

    def test_get_books_genre_shows_all_books_with_genres(self, collector_with_books):
        assert collector_with_books.get_books_genre() == {
            'Гордость и предубеждение и зомби': 'Комедии',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы'}

    def test_get_books_for_children_has_no_books_from_age_rating_genres(self, collector_with_books):
        assert 'Что делать, если ваш кот хочет вас убить' not in collector_with_books.get_books_for_children()

    def test_add_book_in_favorites_added_successfully(self, collector_with_books):
        collector_with_books.add_book_in_favorites(
            'Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector_with_books.favorites

    def test_get_list_of_favorites_books_shows_all_favorite_books(self, collector_with_books):
        assert collector_with_books.get_list_of_favorites_books() == [
            'Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_deleted_successfully(self, collector_with_books):
        collector_with_books.delete_book_from_favorites(
            'Гордость и предубеждение и зомби')
        assert not (
            'Гордость и предубеждение и зомби' in collector_with_books.favorites)
