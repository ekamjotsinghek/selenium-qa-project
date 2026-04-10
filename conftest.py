import pytest
import os
import webbrowser
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    # Set up Chrome options to avoid bot detection
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
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

@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request, driver):
    # Runs after every test — saves screenshot if test failed
    yield
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"\nScreenshot saved: {filename}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Intercepts test results so we can check pass/fail status
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)