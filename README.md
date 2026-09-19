# CodeNimbus QA Automation

This project was created as part of the **QA Automation Intern assignment at CodeNimbus Solutions**.

The project automates two test scenarios for the **Invitation Nation** website using Selenium WebDriver with Python. It also records the test execution results automatically in a Google Sheet.

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Google Sheets API
* gspread
* python-dotenv
* Google Chrome

## Project Structure

```text
CodeNimbus-QA-Automation/
│
├── tests/
│   ├── test_login_dashboard.py
│   ├── test_live_demo.py
│   └── google_sheet_logger.py
│
├── first_test.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Cases

### Test Case 1 – Login and User Dashboard

The test:

1. Opens the Invitation Nation website.
2. Clicks the **Sign In / Sign Up** button.
3. Enters the configured test email and password.
4. Completes the login process.
5. Verifies that the User Dashboard is displayed.
6. Records the test result in Google Sheets.

### Test Case 2 – Invitation Template Live Demo

The test:

1. Opens the Invitation Nation website.
2. Opens the **Invitations** section.
3. Selects the **Wedding** category.
4. Selects an available invitation template.
5. Clicks **Live Demo**.
6. Verifies that a new browser tab is opened.
7. Switches Selenium's focus to the new tab.
8. Verifies that the Live Demo page has loaded.
9. Checks the page URL and page content.
10. Closes the Live Demo tab.
11. Switches back to the original browser tab.
12. Records the test result in Google Sheets.

## Google Sheets Test Result Logging

After every test case, the automation adds a new row to the Google Sheet.

The following information is recorded:

* Date and timestamp
* Test case name
* PASS/FAIL status
* Execution time
* Failure or error reason

This allows the test execution history to be tracked without manually entering the results.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Akhil-Huddar/CodeNimbus-QA-Automation.git
cd CodeNimbus-QA-Automation
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Configure test credentials

Create a `.env` file in the project root:

```text
INVITATION_EMAIL=your_test_email
INVITATION_PASSWORD=your_test_password
```

The `.env` file is excluded from Git using `.gitignore`.

### 5. Configure Google Sheets

A Google service account is used for writing test results.

Place the service account credentials file in the project root with the following name:

```text
credentials.json
```

Share the Google Sheet with the service account email and give it the required access to add test results.

The `credentials.json` file is excluded from Git and must not be uploaded to the public repository.

## Running the Tests

From the project root, run:

```bash
python -m pytest -v -s
```

The two automated test cases will execute and the results will be added to the configured Google Sheet.

## Good Practices Used

The automation uses:

* Explicit waits with `WebDriverWait`
* Selenium expected conditions
* Stable element locators
* Assertions for validation
* Exception handling
* Browser tab/window handling
* Separate test files for different test scenarios
* Automatic PASS/FAIL logging
* Environment variables for test credentials
* Git protection for sensitive files

## Assumptions

* Google Chrome is installed on the system.
* Valid Invitation Nation test credentials are available.
* Internet access is available during test execution.
* Google Sheets API access has been configured.
* The Google service account has access to the test results sheet.
* The Invitation Nation website is available during execution.

## Known Limitations

* The tests depend on the current HTML structure and element locators of the Invitation Nation website.
* The Wedding category and selected template are currently fixed in the automation.
* The Google Sheets logging requires valid service-account credentials and access to the configured sheet.
* The tests require an active internet connection.

## Result

Both test cases were successfully executed using Selenium WebDriver, and the execution results were automatically recorded in Google Sheets.

**Repository:**
https://github.com/Akhil-Huddar/CodeNimbus-QA-Automation
