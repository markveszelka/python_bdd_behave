@feature_add_to_cart @wip
Feature: Add to Cart
  As a shopper
  I want to add products to my cart
  So that I can purchase them later

  @manual @to-be-automated
  Scenario: Add a Single Product to Cart
    Given I am on the product details page for "Push It Messenger Bag"
    When I select a quantity of 1
    And I click the "Add to Cart" button
    Then the product should be added to my cart
    And I should see a confirmation message "You added Push It Messenger Bag to your shopping cart."

  @manual @to-be-automated
  Scenario: Add Multiple Products to Cart
    Given I have added "Push It Messenger Bag" to my cart
    When I add "Hero Hoodie" to my cart
    Then both products should appear in my cart
