@feature_login_page
Feature: Login Page
  As a shopper
  I want to login to my account
  So that I can access my account information

  Background: Open the login page
    Given I am on the "Login" page

  @level_e2e @priority_medium
  Scenario: Check that the URL is correct
    Then The URL of the login page is correct

  @level_e2e @priority_high
  Scenario: Login with invalid credentials
    When I login with "invalid" credentials
    Then I see the invalid credentials error message

  @level_e2e @priority_high
  Scenario: Login with valid credentials
    When I login with "valid" credentials
    Then I am logged in to My Account page

  @level_e2e @priority_medium
  Scenario: Error messages for email and password
    When I login with "empty" credentials
    Then I see Email and Password errors are displayed
