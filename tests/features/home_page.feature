@feature_home_page
Feature: Home Page Verification
  As a shopper
  I want to easily navigate and access key sections of the website from the home page
  So that I can find products, promotions, and account features quickly.

  Background: Open the home page
    Given I am on the "Home" page

  @level_e2e @priority_medium
  Scenario: Verify essential elements on the home page
    Then I see the essential home page elements

  @level_e2e @priority_high
  Scenario Outline: Verify navigation menu buttons
    When I click the "<button>" button
    Then the page with "<url>" is opened
    And  I see the "<header>" header

    Examples:
      | button     | url              | header     |
      | What's New | what-is-new.html | What's New |
      | Women      | women.html       | Women      |
      | Men        | men.html         | Men        |
      | Gear       | gear.html        | Gear       |
      | Training   | training.html    | Training   |
      | Sale       | sale.html        | Sale       |

  @level_e2e @priority_high
  Scenario: Verify navigation to login page from home
    When I click the "Sign In" button
    Then I see the login page
    And  I see the login fields and button
