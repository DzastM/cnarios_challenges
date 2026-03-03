Feature: End-to-end Product Purchasing Flow

    Scenario: Add multiple products to cart and verify cart content
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Wireless Headphones  | 1        |
        | Fitness Band         | 1        |
        | Laptop Backpack      | 1        |
        And I view the cart
        Then the cart should contain
        | Product Name         | Quantity | Price |
        | Wireless Headphones  | 1        | $120  |
        | Fitness Band         | 1        | $60   |
        | Laptop Backpack      | 1        | $100  |
        And total price should be "$280"