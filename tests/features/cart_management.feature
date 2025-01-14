@feature-cart-management @wip
Feature: Cart Management
  As a shopper
  I want to manage my cart
  So that I can update or remove items as needed

  @manual @to-be-automated
  Scenario: Update Quantity in Cart
    Given I have "Push It Messenger Bag" in my cart
    When I change the quantity to 2
    And I click the "Update Shopping Cart" button
    Then the cart total should update accordingly

  @manual @to-be-automated
  Scenario: Remove Item from Cart
    Given I have "Push It Messenger Bag" in my cart
    When I click the "Remove" button for the item
    Then the cart should be empty
    And I should see a message "You have no items in your shopping cart."
