from behave import *
from selenium import webdriver

use_step_matcher("re")

pages = {
    "homepage": "http://127.0.0.1:5000/",
    "blog-page": "http://127.0.0.1:5000/blog"
}


@given('I am on the "(.*)"')
def step_implementation(context, page):
    context.browser = webdriver.Chrome("/Applications/chromedriver")  # lounches a chrome window
    context.browser.get(pages[page])


@then('I am on the "(.*)"')
def step_implementation(context, page):
    assert context.browser.current_url == pages[page]
