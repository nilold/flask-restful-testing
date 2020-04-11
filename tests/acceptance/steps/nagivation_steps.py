from behave import *
from selenium import webdriver

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher("re")


def get_page_by_id(driver, page_id) -> BasePage:
    if page_id == "homepage":
        return HomePage(driver)
    elif page_id == "blog-page":
        return BlogPage(driver)
    elif page_id == "new post page":
        return NewPostPage(driver)

    raise RuntimeError(f"There is no page called: {page_id}")


@given('I am on the "(.*)"')
def step_implementation(context, page_id):
    context.driver = webdriver.Chrome("/Applications/chromedriver")  # lounches a chrome window
    page = get_page_by_id(context.driver, page_id)
    context.driver.get(page.url)


@then('I am on the "(.*)"')
def step_implementation(context, page_id):
    page = get_page_by_id(context.driver, page_id)
    assert context.driver.current_url == page.url
