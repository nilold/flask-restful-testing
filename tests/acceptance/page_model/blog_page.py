from tests.acceptance.locators.blog_page_locators import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + "/blog"

    @property
    def title(self):
        return self.driver.find_element(*BlogPageLocators.TITLE)

    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POSTS)
