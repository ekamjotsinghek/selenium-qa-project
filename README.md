# Selenium QA Automation Project

A professional test automation suite built with Python and Selenium WebDriver, 
designed to validate the core functionality of Google Search using industry-standard 
QA practices including Page Object Model (POM) structure and automated HTML reporting.

## 🛠️ Tech Stack

| Tool                  | Purpose                     |
|-----------------------|-----------------------------|
| Python 3.14           | Programming language        |
| Selenium WebDriver    | Browser automation          |
| Pytest                | Test framework              |
| WebDriver Manager     | Automatic driver management |
| Pytest-HTML           | HTML report generation      |
| Git & GitHub          | Version control             |

## 📁 Project Structure

```
selenium-qa-project/
├── pages/
│   └── google_page.py      # Page Object Model for Google homepage
├── tests/
│   └── test_google.py      # Test cases
├── reports/
│   └── report.html         # Auto-generated HTML test report
├── conftest.py             # Browser setup and teardown
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ⚙️ Installation

1. Clone the repository
2. Navigate into the project folder
3. Install dependencies

## ▶️ Running the Tests

Run all tests with HTML report: The HTML report will open automatically in your browser after tests complete.

## 🧪 Test Cases

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
- **Clean Structure** — Industry standard folder structure for scalability

## 👤 Author

**Ekamjot Singh**  
📧 ekamjotsingh2004.ek@gmail.com  
🔗 [GitHub](https://github.com/ekamjotsinghek)