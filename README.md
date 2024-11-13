# AT Project 1: OrangeHRM Employee Photo Management System

## Overview

The **OrangeHRM Employee Photo Management System** is a web-based application designed to manage employee photos, allowing users to add, edit, and delete photos. The system provides functionality for both employees and Human Resources (HR) teams to manage employee photos, as well as personal information like name, address, and social security details. The photos are stored in a configurable file structure and can be accessed by other systems within the company. This release includes only the photo management features and does not cover other HR data.

## Features

- **Employee Login**: Employees can log into the system using their credentials.
- **HR Photo Management**: HR staff can manage employee photos for all users in the system.
- **Employee Photo Lists**: Photos can be listed based on specific selection criteria.
- **File System Integration**: Photos are stored in a configurable file structure that can be accessed by other systems within the company.

## Technologies Used

- **Python**: Backend and test automation scripting.
- **Selenium**: WebDriver for automating interactions with the OrangeHRM web interface.
- **pytest**: Testing framework to run automated test cases.
- **Pandas**: For reading CSV data for login credentials.
- **CSV**: For storing login test data.
- **Git**: Version control for source code management.
- **ChromeDriver**: For automated browser interactions during testing.



## File Structure

```
AT-Project-1/
│
├── data/
│   └── login_data.csv           # Login credentials data file for tests
│
├── pages/
│   ├── base_page.py             # Base page object class with common methods
│   ├── login_page.py            # Page object for login functionality
│   └── pim_page.py              # Page object for PIM (Personal Information Management) module
│
├── tests/
│   ├── conftest.py              # Pytest setup and screenshot capture logic
│   ├── test_login.py            # Test cases for login functionality
│   └── test_pim.py              # Test cases for PIM functionality (Add, Edit, Delete Employee)
│
└── utils/
    └── result_writer.py         # Utility to update test results in CSV files
```

## Usage

### Running the Tests

To run the tests for the **OrangeHRM Employee Photo Management System**, use the following commands:

1. **Login Test Cases**:
    - Valid and invalid login scenarios are defined in `test_login.py`.
    - The login credentials are fetched from the CSV file `data/login_data.csv`.

    Run the login tests with:

    ```bash
    pytest tests/test_login.py
    ```

2. **PIM (Personal Information Management) Test Cases**:
    - Tests for adding, editing, and deleting employee records are in `test_pim.py`.

    Run the PIM tests with:

    ```bash
    pytest tests/test_pim.py
    ```

### Writing Test Results

Test results are updated in a CSV file using the `update_test_result()` function defined in `utils/result_writer.py`. The results are logged for each test case ID.

---

## Test Cases

### Login Test Cases

#### TC_Login_01: Successful Employee Login

- **Test Objective**: Verify that an employee can successfully log into the OrangeHRM portal.
- **Preconditions**: 
  - Valid ESS-User account available.
  - OrangeHRM site is launched in a compatible browser.
- **Steps**:
  1. Enter the username "Admin".
  2. Enter the password "admin123".
  3. Click the "Login" button.
- **Expected Result**: User is logged in successfully, and redirected to the dashboard.

#### TC_Login_02: Invalid Employee Login

- **Test Objective**: Verify that invalid login attempts show an appropriate error message.
- **Preconditions**: 
  - Valid ESS-User account available.
  - OrangeHRM site is launched in a compatible browser.
- **Steps**:
  1. Enter the username "Admin".
  2. Enter an incorrect password "Invalid password".
  3. Click the "Login" button.
- **Expected Result**: An error message "Invalid credentials" is displayed.

### PIM Test Cases

#### TC_PIM_01: Add a New Employee

- **Test Objective**: Verify that an HR can add a new employee to the system.
- **Preconditions**: 
  - Valid ESS-User account available.
  - OrangeHRM site is launched in a compatible browser.
- **Steps**:
  1. Navigate to the PIM module.
  2. Click "Add" and enter employee details.
  3. Click "Save".
- **Expected Result**: The new employee is added successfully, and a success message is displayed.

#### TC_PIM_02: Edit an Existing Employee

- **Test Objective**: Verify that an HR can edit an existing employee's information.
- **Preconditions**: 
  - Valid ESS-User account available.
  - OrangeHRM site is launched in a compatible browser.
- **Steps**:
  1. Navigate to the PIM module.
  2. Edit the employee's information.
  3. Save the changes.
- **Expected Result**: The employee details are updated, and a success message is displayed.

#### TC_PIM_03: Delete an Existing Employee

- **Test Objective**: Verify that an HR can delete an existing employee.
- **Preconditions**: 
  - Valid ESS-User account available.
  - OrangeHRM site is launched in a compatible browser.
- **Steps**:
  1. Navigate to the PIM module.
  2. Select an employee to delete.
  3. Click "Delete" and confirm.
- **Expected Result**: The employee is deleted successfully, and a success message is displayed.

---

## Conclusion

This repository provides a comprehensive implementation of the **OrangeHRM Employee Photo Management System**. It includes test cases for login functionality and employee management (PIM). Automation scripts using Selenium and pytest ensure the system works as expected.
