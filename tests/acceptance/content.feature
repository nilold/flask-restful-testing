Feature: Test that pages have correct content

  Scenario: Blog page has a correct title
    Given I am on the "blog-page"
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"

  Scenario: Homepage has a correct title
    Given I am on the "homepage"
    Then There is a title shown on the page
    And The title tag has content "This is the homepage"


  Scenario: Blog page loads posts
    Given I am on the "blog-page"
    And I wait for the posts to load
    Then I can see there is a posts section on the page
