from selenium.webdriver.common.by import By
from tests.acceptance.locators.base_page_locators import BasePageLocators


class HomePageLocators(BasePageLocators):
    BLOG_LINK = By.ID, "blog-link"

