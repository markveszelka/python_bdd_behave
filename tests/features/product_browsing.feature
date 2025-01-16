@feature_product_browsing @wip
Feature: Product Browsing
  As a shopper
  I want to browse products by category
  So that I can find items of interest

  @manual @to_be_automated
  Scenario: Browse Products by Category
    Given I am on the "Home" page
    When  I navigate to the "Men > Tops > T-Shirts" category
    Then  I should see a list of T-Shirts for men
    And   each product should display its name, price, and image

  @manual @to_be_automated
  Scenario: Search for a Product
    Given I am on the "Home" page
    When  I search for "Yoga Pants"
    Then  I should see a list of products related to "Yoga Pants"

  @manual @to_be_automated
  Scenario: View Product Details
    Given I am on the product listing page for "Yoga Pants"
    When  I click on a product
    Then  I should be taken to the product details page
    And   the page should display the product name, price, description, and available sizes
