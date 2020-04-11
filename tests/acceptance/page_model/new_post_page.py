from selenium.webdriver.common.by import By

from tests.acceptance.locators.new_post_page_locators import NewPagePostLocator
from tests.acceptance.page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + "/post"

    @property
    def form(self):
        return self.driver.find_element(*NewPagePostLocator.NEW_POST_FORM)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPagePostLocator.SUBMIT_BUTTON)