import pytest
from pages.wiki_page import WikiPage
from selenium.webdriver.common.by import By

def test_homepage_loads(driver):
    # Checks if Wikipedia homepage loads and title contains "Wikipedia"
    wiki = WikiPage(driver)
    wiki.open()
    assert "Wikipedia" in wiki.get_title()

def test_search_bar_exists(driver):
    # Checks if the search bar is visible on the Wikipedia homepage
    wiki = WikiPage(driver)
    wiki.open()
    search_bar = wiki.get_search_bar()
    assert search_bar.is_displayed()

def test_search_returns_article(driver):
    # Checks if searching returns a valid Wikipedia article
    wiki = WikiPage(driver)
    wiki.open()
    wiki.search("Python programming")
    assert "Python" in wiki.get_heading()

def test_title_changes_after_search(driver):
    # Checks if page title updates correctly after performing a search
    wiki = WikiPage(driver)
    wiki.open()
    wiki.search("Python programming")
    assert "Python" in wiki.get_title()

def test_search_bar_accepts_input(driver):
    # Checks if the search bar correctly accepts and holds typed input
    wiki = WikiPage(driver)
    wiki.open()
    search_bar = wiki.get_search_bar()
    search_bar.send_keys("Selenium")
    assert search_bar.get_attribute("value") == "Selenium"