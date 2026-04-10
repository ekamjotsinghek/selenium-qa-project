import pytest
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    # Set up Chrome options to avoid bot detection
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Hide automation signals from websites
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    yield driver

    # Close the browser
    driver.quit()

    # Automatically open the HTML report
    report_path = os.path.abspath("reports/report.html")
    webbrowser.open(f"file://{report_path}")