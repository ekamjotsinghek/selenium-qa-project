# import pytest
# from pages.google_page import GooglePage
# from selenium.webdriver.common.by import By

# def test_homepage_loads(driver):
#     # Checks if Google homepage loads and the title contains "Google"
#     google = GooglePage(driver)
#     google.open()
#     assert "Google" in google.get_title()

# def test_search_bar_exists(driver):
#     # Checks if the search bar is visible on the Google homepage
#     google = GooglePage(driver)
#     google.open()
#     search_bar = google.driver.find_element(By.NAME, "q")
#     assert search_bar.is_displayed()

# def test_search_returns_results(driver):
#     # Checks if searching returns at least one result on the page
#     google = GooglePage(driver)
#     google.open()
#     google.search("Python tutorials")
#     results = google.get_results()
#     assert len(results) > 0

# def test_title_changes_after_search(driver):
#     # Checks if the page title updates correctly after performing a search
#     google = GooglePage(driver)
#     google.open()
#     google.search("Python tutorials")
#     assert "Python tutorials" in google.get_title()

# def test_search_bar_accepts_input(driver):
#     # Checks if the search bar correctly accepts and holds typed input
#     google = GooglePage(driver)
#     google.open()
#     search_bar = google.driver.find_element(By.NAME, "q")
#     search_bar.send_keys("Selenium Python")
#     assert search_bar.get_attribute("value") == "Selenium Python"