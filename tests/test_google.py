import pytest
from pages.google_page import GooglePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger("test_google")

@pytest.mark.local
def test_homepage_loads(driver):
    # Checks if Google homepage loads and the title contains "Google"
    logger.info("Starting test: test_homepage_loads")
    google = GooglePage(driver)
    google.open()
    logger.info("Navigated to Google homepage")
    assert "Google" in google.get_title()
    logger.info("PASSED: Page title contains Google")

@pytest.mark.local
def test_search_bar_exists(driver):
    # Checks if the search bar is visible on the Google homepage
    logger.info("Starting test: test_search_bar_exists")
    google = GooglePage(driver)
    google.open()
    search_bar = google.driver.find_element(By.NAME, "q")
    logger.info("Located search bar element")
    assert search_bar.is_displayed()
    logger.info("PASSED: Search bar is visible")

@pytest.mark.local
def test_search_returns_results(driver):
    # Checks if searching returns at least one result on the page
    logger.info("Starting test: test_search_returns_results")
    google = GooglePage(driver)
    google.open()
    google.search("Python tutorials")
    logger.info("Searched for: Python tutorials")
    results = google.get_results()
    assert len(results) > 0
    logger.info("PASSED: Search returned at least one result")

@pytest.mark.local
def test_title_changes_after_search(driver):
    # Checks if the page title updates correctly after performing a search
    logger.info("Starting test: test_title_changes_after_search")
    google = GooglePage(driver)
    google.open()
    google.search("Python tutorials")
    logger.info("Searched for: Python tutorials")
    assert "Python tutorials" in google.get_title()
    logger.info("PASSED: Page title updated correctly")

@pytest.mark.local
def test_search_bar_accepts_input(driver):
    # Checks if the search bar correctly accepts and holds typed input
    logger.info("Starting test: test_search_bar_accepts_input")
    google = GooglePage(driver)
    google.open()
    search_bar = google.driver.find_element(By.NAME, "q")
    search_bar.send_keys("Selenium Python")
    logger.info("Typed Selenium Python into search bar")
    assert search_bar.get_attribute("value") == "Selenium Python"
    logger.info("PASSED: Search bar accepted and held input correctly")