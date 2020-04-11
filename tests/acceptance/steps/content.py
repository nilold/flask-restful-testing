from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher("re")


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@step('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@step('I can see there is a post with title "(.*)" in the posts')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert (len(posts_with_title) > 0)
    assert any([post.is_displayed() for post in posts_with_title])