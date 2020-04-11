from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher("re")


@when('I click on "(.*)" link')
def step_implementation(context, link_text):
    page = BasePage(context.driver)
    nav_links = page.navigation
    for link in nav_links:
        print("found link text:" + link.text)
        print("desired link text:" + link_text)
        if link.text == link_text:
            link.click()
            return

    raise RuntimeError(f"Link with text {link_text} not found on {context.driver.current_url}")


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()