from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("I am on the homepage")
def step_implementation(context):
    context.browser = webdriver.Chrome("/Applications/chromedriver")  # lounches a chrome window
    context.browser.get("http://127.0.0.1:5000/")


@then("I am on the blog page")
def step_implementation(context):
    expected_url = "http://127.0.0.1:5000/blog"
    assert context.browser.current_url == expected_url
