@feature_cart_management @wip
Feature: Cart Management
  As a shopper
  I want to manage my cart
  So that I can adjust Products as needed

  Background: Add a Product to Cart
    Given I have added "Push It Messenger Bag" to my cart

  @manual @to_be_automated
  Scenario: Add a Single Product to Cart
    Then the product should be added to my cart
    And I should see a confirmation message "You added Push It Messenger Bag to your shopping cart."

  @manual @to_be_automated
  Scenario: Remove Item from Cart
    When I click the "Remove" button for the item
    Then the cart should be empty
    And I should see a message "You have no items in your shopping cart."

  @manual @to_be_automated
  Scenario: Add Multiple Products to Cart
    When I add "Hero Hoodie" to my cart
    Then both products should appear in my cart

  @manual @to_be_automated
  Scenario: Update Quantity in Cart
    When I change the quantity to 2
    And I click the "Update Shopping Cart" button
    Then the cart total should update accordingly
