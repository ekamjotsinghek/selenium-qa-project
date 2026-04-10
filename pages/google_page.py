# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class GooglePage:
#     def __init__(self, driver):
#         # Sets up the browser and Google URL when the object is created
#         self.driver = driver
#         self.url = "https://www.google.com"

#     def open(self):
#         # Navigates Chrome to Google.com
#         self.driver.get(self.url)

#     def search(self, query):
#         # Finds the search bar, clears it, types the query and hits Enter
#         search_bar = self.driver.find_element(By.NAME, "q")
#         search_bar.clear()
#         search_bar.send_keys(query)
#         search_bar.send_keys(Keys.ENTER)
#         WebDriverWait(self.driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//h3"))
#         )

#     def get_title(self):
#         # Returns the current page title from the browser tab
#         return self.driver.title

#     def get_results(self):
#         # Returns all search result headings found on the page
#         return self.driver.find_elements(By.XPATH, "//h3")