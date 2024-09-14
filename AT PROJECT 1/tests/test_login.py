#tests/test_login.py
import pytest
import pandas as pd
from pages.login_page import LoginPage
from utils.result_writer import update_test_result


def get_login_data():
    login_data = []
    # Read the CSV file with login data
    df = pd.read_csv('data/login_data.csv')
    for index, row in df.iterrows():
        login_data.append((row['username'], row['password'], index + 1))
    return login_data


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username, password, test_id", get_login_data())
    def test_login(self, username, password, test_id):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        if username == "Admin" and password == "admin123":
            assert "dashboard" in self.driver.current_url, "Login failed for valid credentials."
            result = "Passed"
        else:
            error_message = login_page.get_error_message()
            assert "Invalid credentials" in error_message, f"Unexpected error message: {error_message}"
            result = "Passed" if "Invalid credentials" in error_message else "Failed"

        tester_name = "Sowndharya"

        # Update the test result in the CSV file
        update_test_result(test_id, result, tester_name)

        assert result == "Passed"
