import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


class Utils:
    def login(driver):
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        username.clear()
        username.send_keys("teacher")
        password = driver.find_element(by=By.ID, value="password")
        password.clear()
        password.send_keys("moodle")
        password.send_keys(Keys.RETURN)


class GradeSettingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("./chromedriver"))
        self.driver.maximize_window()
        self.driver.get("https://school.moodledemo.net/course/modedit.php?update=852&return=1")
        Utils.login(self.driver)

    def test_1(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("-1")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=852&forceview=1" == driver.current_url

    def test_2(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("25")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=852&forceview=1" == driver.current_url

    def test_3(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("0")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings."
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_4(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings."
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_5(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("75")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["The grade to pass can not be greater than the maximum possible grade 50"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_6(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("abc")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "You must enter a number here.",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_7(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("-5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("-10")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_8(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("-5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("15")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_9(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("-10")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_10(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("50")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_11(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("102")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_12(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("-10")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_13(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("50")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_14(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("51")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_15(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("-10")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_16(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("10")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = ["Invalid grade value. This must be an integer between 1 and 100"]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_17(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("-5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("0")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_18(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("-5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_19(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("0")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_20(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_21(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("0")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_22(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_23(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("0")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_24(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_25(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("-5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("abc")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
            "You must enter a number here.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_26(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("101")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("abc")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
            "You must enter a number here.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_27(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()
        maximum_grade.send_keys("50.5")

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("abc")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
            "You must enter a number here.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def test_28(self):
        driver = self.driver

        wait = WebDriverWait(driver, 10)
        openGradeSetting = wait.until(EC.element_to_be_clickable((By.ID, "collapseElement-7")))
        openGradeSetting.click()

        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 10)
        maximum_grade = wait.until(EC.element_to_be_clickable((By.ID, "id_grade_modgrade_point")))

        maximum_grade.clear()

        grade_pass = driver.find_element(by=By.ID, value="id_gradepass")
        grade_pass.clear()
        grade_pass.send_keys("abc")

        save_and_display = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_display.click()

        error_list = [
            "Invalid grade value. This must be an integer between 1 and 100",
            "This activity does not have a valid grade to pass set. It may be set in the Grade section of the activity settings.",
            "You must enter a number here.",
        ]

        try:
            errors = driver.find_elements(
                by=By.XPATH, value="//div[contains(@class, 'form-control-feedback')][normalize-space()]"
            )
        except NoSuchElementException:
            self.fail("Element not found")

        if len(errors) != len(error_list):
            self.fail("Failed")

        for error in errors:
            if error.text not in error_list:
                self.fail("Failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
