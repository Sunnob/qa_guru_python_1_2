import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после теста
    driver.quit()

@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")


@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"