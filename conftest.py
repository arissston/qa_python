import pytest

from main import BooksCollector


@pytest.fixture(scope='session')
def collector():
    return BooksCollector()


@pytest.fixture(scope='session')
def collector_with_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    return collector
