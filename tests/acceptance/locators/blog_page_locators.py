from selenium.webdriver.common.by import By
from tests.acceptance.locators.base_page_locators import BasePageLocators


class BlogPageLocators(BasePageLocators):
    HOME_LINK = By.ID, "home-link"
    ADD_POST_LINK = By.ID, "add-post-link"
    POSTS_SECTION = By.ID, "posts"
    POSTS = By.CLASS_NAME, "post"
