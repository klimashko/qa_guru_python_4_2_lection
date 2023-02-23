import random

import pytest


@pytest.fixture
def browser():
    print("Открыли браузер")
    yield "Chrome"
    print("Закрыли браузер")


@pytest.fixture
def teardown():
    yield
    print("do_something")


@pytest.fixture
def get_admin(browser, teardown):  # аргумент teardown это фикстура, она лежит в файле conftest
    return random.randint(0, 100)


def test_simple(browser, get_admin):
    assert get_admin == 5, "Айди админа ожидался 5, условие не выполнилось"
    assert browser == "Chrome"
    assert 1 == 1, "Единица не должна быть равна 2"


def test_another(browser, get_admin):
    assert get_admin == 5, "Айди администратора ожидался 5"
    assert 1 == 1, "Условие не выполнилось"

