Feature: Product Filtering & Search

#high priority 
    Scenario: Filter products by category
        Given I am on the product listing page
        When I filter products by category "Electronics"
        Then only products from "Electronics" category should be displayed

#high priority 
    Scenario: Filter products by price range
        Given I am on the product listing page
        When I filter products with price range "₹5000 - ₹50000"
        Then only products priced between ₹5000 and ₹50000 should be displayed

    Scenario: Filter products by minimum rating
        Given I am on the product listing page
        When I filter products with minimum rating of 4 stars
        Then only products with 4 stars or higher should be displayed

    Scenario: Show only in-stock products
        Given I am on the product listing page
        When I apply filter to show only in-stock products
        Then only products that are currently in stock should be displayed

#high priority 
    Scenario: Reset filters
        Given I am on the product listing page
        And I have applied filters of category, price and stock
        When I click the "Reset" button
        Then all filters should be cleared 
        And the full product listing should be displayed