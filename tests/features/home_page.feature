@feature_home_page
Feature: Home Page

  # Running cmd 'behave --tags=priority_high' will run just the scenarios tagged @priority_high
  @priority_high
  Scenario: Navigate to the Login page
    Given I am on the home page
    When I click the login button
    Then I should see the login page