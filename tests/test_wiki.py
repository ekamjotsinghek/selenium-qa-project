import pytest
from pages.wiki_page import WikiPage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger("test_wiki")

def test_homepage_loads(driver):
    # Checks if Wikipedia homepage loads and title contains "Wikipedia"
    logger.info("Starting test: test_homepage_loads")
    wiki = WikiPage(driver)
    wiki.open()
    logger.info("Navigated to Wikipedia homepage")
    assert "Wikipedia" in wiki.get_title()
    logger.info("PASSED: Page title contains Wikipedia")

def test_search_bar_exists(driver):
    # Checks if the search bar is visible on the Wikipedia homepage
    logger.info("Starting test: test_search_bar_exists")
    wiki = WikiPage(driver)
    wiki.open()
    search_bar = wiki.get_search_bar()
    logger.info("Located search bar element")
    assert search_bar.is_displayed()
    logger.info("PASSED: Search bar is visible")

def test_search_returns_article(driver):
    # Checks if searching returns a valid Wikipedia article
    logger.info("Starting test: test_search_returns_article")
    wiki = WikiPage(driver)
    wiki.open()
    wiki.search("Python programming")
    logger.info("Searched for: Python programming")
    assert "Python" in wiki.get_heading()
    logger.info("PASSED: Article heading contains Python")

def test_title_changes_after_search(driver):
    # Checks if page title updates correctly after performing a search
    logger.info("Starting test: test_title_changes_after_search")
    wiki = WikiPage(driver)
    wiki.open()
    wiki.search("Python programming")
    logger.info("Searched for: Python programming")
    assert "Python" in wiki.get_title()
    logger.info("PASSED: Page title updated correctly")

def test_search_bar_accepts_input(driver):
    # Checks if the search bar correctly accepts and holds typed input
    logger.info("Starting test: test_search_bar_accepts_input")
    wiki = WikiPage(driver)
    wiki.open()
    search_bar = wiki.get_search_bar()
    search_bar.send_keys("Selenium")
    logger.info("Typed Selenium into search bar")
    assert search_bar.get_attribute("value") == "Selenium"
    logger.info("PASSED: Search bar accepted and held input correctly")