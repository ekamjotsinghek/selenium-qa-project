from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikiPage:
    def __init__(self, driver):
        # Sets up the browser and Wikipedia URL when the object is created
        self.driver = driver
        self.url = "https://www.wikipedia.org"

    def open(self):
        # Navigates Chrome to Wikipedia.org
        self.driver.get(self.url)

    def search(self, query):
        # Finds the search bar, clears it, types the query and hits Enter
        search_bar = self.driver.find_element(By.NAME, "search")
        search_bar.clear()
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)
        # Wait up to 30 seconds for results to load
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )

    def get_title(self):
        # Returns the current page title from the browser tab
        return self.driver.title

    def get_heading(self):
        # Returns the main heading of the Wikipedia article
        return self.driver.find_element(By.ID, "firstHeading").text

    def get_search_bar(self):
        # Returns the search bar element
        return self.driver.find_element(By.NAME, "search")