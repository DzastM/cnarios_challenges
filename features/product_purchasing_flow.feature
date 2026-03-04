Feature: End-to-end Product Purchasing Flow

    Scenario: Add product to cart and verify
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Wireless Headphones  | 1        |
        And I view the cart
        Then the cart should contain
        | Product Name         | Quantity | Price |
        | Wireless Headphones  | 1        | $120  |
        And total price should be "$120"

    Scenario: Increase and decrease product quantity in cart
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Smartphone Stand     | 1        |
        And I view the cart
        And I increase the quantity of "Smartphone Stand" to 3
        Then the cart should contain
        | Product Name         | Quantity | Price |
        | Smartphone Stand     | 3        | $135   |
        And total price should be "$135"
        When I decrease the quantity of "Smartphone Stand" to 2
        Then the cart should contain
        | Product Name         | Quantity | Price |
        | Smartphone Stand     | 2        | $90   |
        And total price should be "$90"

    Scenario: Remove product from cart
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Laptop Backpack      | 1        |
        And I view the cart
        And I decrease the quantity of "Laptop Backpack" to 0
        Then the cart should be empty

    Scenario: Billing form validation
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Bluetooth Speaker    | 1        |
        And I view the cart
        And I proceed to address
        Then "Proceed to Payment" button should be disabled

    Scenario: Successful payment flow
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Fitness Band         | 1        |
        And I view the cart
        And I proceed to address
        And I fill in the billing form with data
        | First Name | Last Name | Address              |
        | John       | Doe       | 123 Main St, Anytown |
        And I click "Proceed to payment" button
        And I click "Pay Now" button
        Then success message should be displayed with billing details

    Scenario: Failed payment flow
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Wireless Headphones  | 1        |
        And I view the cart
        And I proceed to address
        And I fill in the billing form with data
        | First Name | Last Name | Address              |
        | John       | Doe       | 123 Main St, Anytown |
        And I click "Proceed to payment" button
        And I click "Cancel" button
        Then failure message should be displayed with "Go Home" button

    Scenario: Go Home resets flow
        Given I am on the product purchasing page
        When I add products to the cart
        | Product Name         | Quantity |
        | Wireless Headphones  | 1        |
        And I view the cart
        And I proceed to address
        And I fill in the billing form with data
        | First Name | Last Name | Address              |
        | John       | Doe       | 123 Main St, Anytown |
        And I click "Proceed to payment" button
        And I click "Pay Now" button
        And I click "Go Home" button
        Then I should be redirected to the homepage
        And the cart count should be reset to 0