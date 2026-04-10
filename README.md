# Selenium QA Automation Project

A professional test automation suite built with Python and Selenium WebDriver,
designed to validate core web functionality across multiple websites using
industry-standard QA practices including Page Object Model (POM) structure,
automated HTML reporting, CI/CD integration via GitHub Actions, screenshot
capture on failure, and a detailed logging system.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14 | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| WebDriver Manager | Automatic driver management |
| Pytest-HTML | HTML report generation |
| GitHub Actions | CI/CD pipeline |
| Git & GitHub | Version control |

## 📁 Project Structure

````
selenium-qa-project/
├── .github/
│   └── workflows/
│       └── run_tests.yml   # CI/CD pipeline configuration
├── pages/
│   ├── google_page.py      # Page Object Model for Google homepage
│   └── wiki_page.py        # Page Object Model for Wikipedia homepage
├── tests/
│   ├── test_google.py      # Google test cases (local only)
│   └── test_wiki.py        # Wikipedia test cases (local + CI/CD)
├── utils/
│   ├── __init__.py         # Package initializer
│   └── logger.py           # Logging utility
├── reports/
│   └── report.html         # Auto-generated HTML test report
├── screenshots/            # Auto-captured on test failure
├── logs/                   # Auto-generated test run logs
├── conftest.py             # Browser setup, teardown and screenshot capture
├── pytest.ini              # Pytest configuration and custom markers
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
````

## ⚙️ Installation

1. Clone the repository
```
git clone https://github.com/ekamjotsinghek/selenium-qa-project.git
```
2. Navigate into the project folder
```
cd selenium-qa-project
```
3. Install dependencies
```
pip install -r requirements.txt
```

## ▶️ Running the Tests

Run Wikipedia tests locally with HTML report:
```
python -m pytest tests/test_wiki.py -v --html=reports/report.html --self-contained-html
```
Run Google tests locally only:
```
python -m pytest tests/test_google.py -v --html=reports/report.html --self-contained-html
```
Run all local tests:
```
python -m pytest -v --html=reports/report.html --self-contained-html
```

The HTML report will open automatically in your browser after tests complete.
Screenshots are saved to the `screenshots/` folder on any test failure.
Logs are saved to the `logs/` folder after every test run.

## 🌐 Test Suites

| Suite | Website | Environment |
|-------|---------|-------------|
| test_wiki.py | Wikipedia | Local + CI/CD |
| test_google.py | Google | Local only (bot detection prevents cloud execution) |

## 🧪 Test Cases

### Wikipedia Tests
| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| test_homepage_loads | Verifies Wikipedia homepage loads correctly | Page title contains "Wikipedia" |
| test_search_bar_exists | Verifies search bar is visible on homepage | Search bar is displayed |
| test_search_returns_article | Verifies searching returns a valid article | Article heading contains search query |
| test_title_changes_after_search | Verifies page title updates after search | Title contains search query |
| test_search_bar_accepts_input | Verifies search bar accepts typed input | Input matches typed text |

### Google Tests (Local Only)
| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| test_homepage_loads | Verifies Google homepage loads correctly | Page title contains "Google" |
| test_search_bar_exists | Verifies search bar is visible on homepage | Search bar is displayed |
| test_search_returns_results | Verifies searching returns results | At least one result appears |
| test_title_changes_after_search | Verifies page title updates after search | Title contains search query |
| test_search_bar_accepts_input | Verifies search bar accepts typed input | Input matches typed text |

## ✨ Key Features

- **Page Object Model (POM)** — Separates page logic from test logic for maintainability
- **Smart Waits** — Uses WebDriverWait to handle slow connections reliably
- **Bot Detection Bypass** — Chrome configured to run without triggering CAPTCHA
- **Auto HTML Reports** — Test report opens automatically after every run
- **Screenshot on Failure** — Automatically captures browser screenshot when any test fails
- **Logging System** — Records detailed test execution logs with timestamps to file and console
- **CI/CD Pipeline** — Tests run automatically on every GitHub push via GitHub Actions
- **Multi-site Coverage** — Tests across both Google and Wikipedia
- **Clean Structure** — Industry standard folder structure for scalability

## 👤 Author

**Ekamjot Singh**  
📧 ekamjotsingh2004.ek@gmail.com  
🔗 [GitHub](https://github.com/ekamjotsinghek)
