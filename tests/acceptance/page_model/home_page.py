from tests.acceptance.locators.home_page_locators import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + "/"

    @property
    def title(self):
        return self.driver.find_element(*HomePageLocators.TITLE)

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.BLOG_LINK)
