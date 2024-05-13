import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def browser():
    # Setup Selenium
    if os.getenv("CI"):
        service = Service()
    else:
        service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestIndex:
    # Setup browser
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.browser.get("http://127.0.0.1:5000")

    # Check if page title is correctly displayed
    def test_page_title(self):
        expected_title = "Tasks Dashboard"
        assert (
            self.browser.title == expected_title
        ), f"Expected page title to be '{expected_title}' but got '{self.browser.title}'"

    # Check if username is correctly displayed
    def test_username_displayed(self):
        username_span = self.browser.find_element(
            By.CSS_SELECTOR, "span.username-placeholder"
        )
        expected_username = "username"
        assert username_span.text == expected_username

    # Check if search bar is correctly displayed
    def test_search_bar_displayed(self):
        search_bar = self.browser.find_element(By.ID, "search-tasklists")
        assert search_bar.is_displayed()

    # Check if task lists are correctly displayed
    def test_task_categories_displayed(self):
        task_categories = self.browser.find_element(By.ID, "task-categories")
        assert task_categories.is_displayed()

    # Check if task itms are correctly displayed
    def test_task_item_displayed(self):
        task_item = self.browser.find_element(By.CSS_SELECTOR, ".task-item")
        assert task_item.is_displayed()

    # Check if dropdown is correctly displayed
    def test_dropdown_displayed(self):
        dropdown_button = self.browser.find_element(By.CSS_SELECTOR, ".dropdown-toggle")
        assert dropdown_button.is_displayed(), "Dropdown button is not displayed"
