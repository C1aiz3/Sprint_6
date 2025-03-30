import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    firefox = webdriver.Firefox()
    yield firefox
    firefox.quit()