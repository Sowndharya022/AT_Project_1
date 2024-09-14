#tests/test_pim.py
import pytest
from pages.pim_page import PIMPage
from pages.login_page import LoginPage
from utils.result_writer import update_test_result


@pytest.mark.usefixtures("setup")
class TestPIM:

    def test_add_employee(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        pim_page = PIMPage(self.driver)
        pim_page.go_to_pim()

        pim_page.add_employee("Sowndharya", "Mohan", "M")
        pim_page.add_personal_details()

        try:
            pim_page.click_element(pim_page.SAVE_BUTTON)

            success = True
        except Exception as e:
            print(f"Error clicking the edit button: {e}")
            success = False

        # Update test result based on the outcome
        if success:
            update_test_result("TC_PIM_01", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_01", "Failed - Employee not found", "Sowndharya")

    def test_edit_employee(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        pim_page = PIMPage(self.driver)
        pim_page.go_to_pim()

        pim_page.edit_employee("Sowndharya","Mohan","M")


        try:
            pim_page.click_element(pim_page.EDIT_BUTTON)

            success = True  # Replace with actual success check logic
        except Exception as e:
            print(f"Error clicking the edit button: {e}")
            success = False

        # Update test result based on the outcome
        if success:
            update_test_result("TC_PIM_02", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_02", "Failed - Employee not found", "Sowndharya")

    def test_delete_employee(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        pim_page = PIMPage(self.driver)
        pim_page.go_to_pim()

        try:
            pim_page.click_element(pim_page.yes_delete)

            success = True  # Replace with actual success check logic
        except Exception as e:
            print(f"Error clicking the edit button: {e}")
            success = False

        # Update test result based on the outcome
        if success:
            update_test_result("TC_PIM_03", "Passed", "Sowndharya")
        else:
            update_test_result("TC_PIM_03", "Failed - Employee not found", "Sowndharya")