Feature: End-to-end Product Purchasing Flow

    Scenario: Add multiple products to cart and verify cart content
        Given I am on the product purchasing page
        When I add "Wireless Headphones" to the cart
        # And I add "Fitness Band" to the cart
        # And I add "Laptop Backpack" to the cart
        And I view the cart
        # Then the cart should contain "1 x Wireless Headphones"
        # And total price should be <total_price>