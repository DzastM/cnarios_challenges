Feature: Product Listing Pagination

    Scenario: Count products in each category
        Given I am on the product listing page
        When I count the number of products in each category
        Then the product counts should match information from product data file

    Scenario: Find specific product and identify its page
        Given I am on the product listing page
        When I search for product "Under Armour Running Shoes"
        Then I should find the product with correct data
            | Product Name               | Price  | Category | Stars |
            | Under Armour Running Shoes | $99.99 | Clothing | 5     |
        And product was found on page <2>

    Scenario: Find highest-rated product in each category
        Given I am on the product listing page
        When I identify the highest-rated products in each category
        Then the highest-rated products should match information given in table
            | Category    | Product Names                         |
            | Books       | The Pragmatic Programmer              |
            | Sports      | Wilson Pro Staff Tennis Racket        |
            | Home        | Samsung Smart Refrigerator            |
            | Home        | KitchenAid Stand Mixer                |
            | Electronics | Sony PlayStation 5                    |
            | Sports      | Callaway Golf Set                     |
            | Clothing    | Nike Air Force 1 Sneakers             |
            | Clothing    | Patagonia Fleece Sweater              |
            | Sports      | Adidas Predator Football              |
            | Books       | Sapiens: A Brief History of Humankind |
            | Home        | Breville Barista Express              |
            | Books       | Atomic Habits                         |
            | Electronics | GoPro HERO11 Black                    |
            | Clothing    | The North Face Jacket                 |
            | Home        | Instant Pot Duo                       |
            | Electronics | Bose QuietComfort 45                  |
            | Electronics | Apple MacBook Air M2                  |
            | Electronics | Apple iPhone 14 Pro                   |
            | Clothing    | Under Armour Running Shoes            |
            | Home        | Philips Air Fryer XXL                 |
            | Electronics | Samsung Galaxy S23 Ultra              |
            | Books       | Clean Code                            |
            | Sports      | Nike Mercurial Football Boots         |
            | Home        | Dyson V15 Detect Vacuum               |

    Scenario: Find the most expensive product in each category
        Given I am on the product listing page
        When I identify the most expensive products in each category
        Then the most expensive products should match given information
            | Category    | Product name               | Price    |
            | Books       | Clean Code                 | $34.99   |
            | Home        | Samsung Smart Refrigerator | $1799.99 |
            | Clothing    | The North Face Jacket      | $129.99  |
            | Electronics | Dell XPS 13 Laptop         | $1199.99 |
            | Sports      | Callaway Golf Set          | $499.99  |

    Scenario: Validate pagination controls
        Given I am on the product listing page
        When I click page <3>
        Then products listed on page <3> should match given information
            | Product Name                        | Category    | Price   | Stars |
            | The North Face Jacket               | Clothing    | $129.99 | 5     |
            | Zero to One                         | Books       | $21.99  | 4     |
            | Haier 1.5 Ton Split AC              | Home        | $499.99 | 4     |
            | Instant Pot Duo                     | Home        | $129.99 | 5     |
            | Apple Watch Series 9                | Electronics | $499.99 | 4     |
            | Microsoft Xbox Series X             | Electronics | $499.99 | 4     |
            | Everlast Boxing Gloves              | Sports      | $49.99  | 4     |
            | The Subtle Art of Not Giving a F*ck | Books       | $12.99  | 4     |
            | Bose QuietComfort 45                | Electronics | $299.99 | 5     |
            | Uniqlo Ultra Light Down Jacket      | Clothing    | $59.99  | 4     |
        When I click "Next" button
        Then products listed on page <4> should match given information
            | Product Name               | Category    | Price    | Stars |
            | Spalding NBA Basketball    | Sports      | $29.99   | 4     |
            | Apple MacBook Air M2       | Electronics | $1099.99 | 5     |
            | Apple iPhone 14 Pro        | Electronics | $999.99  | 5     |
            | Reebok Yoga Mat            | Sports      | $24.99   | 4     |
            | H&M Cotton Shirt           | Clothing    | $24.99   | 3     |
            | Puma Sports T-Shirt        | Clothing    | $29.99   | 3     |
            | Under Armour Running Shoes | Clothing    | $99.99   | 5     |
            | Philips Air Fryer XXL      | Home        | $199.99  | 5     |
            | Yonex Badminton Racket     | Sports      | $59.99   | 4     |
            | Sony WH-1000XM5 Headphones | Electronics | $399.99  | 5     |
        When I click "Previous" button
        Then products listed on page <3> should match given information
            | Product Name                        | Category    | Price   | Stars |
            | The North Face Jacket               | Clothing    | $129.99 | 5     |
            | Zero to One                         | Books       | $21.99  | 4     |
            | Haier 1.5 Ton Split AC              | Home        | $499.99 | 4     |
            | Instant Pot Duo                     | Home        | $129.99 | 5     |
            | Apple Watch Series 9                | Electronics | $499.99 | 4     |
            | Microsoft Xbox Series X             | Electronics | $499.99 | 4     |
            | Everlast Boxing Gloves              | Sports      | $49.99  | 4     |
            | The Subtle Art of Not Giving a F*ck | Books       | $12.99  | 4     |
            | Bose QuietComfort 45                | Electronics | $299.99 | 5     |
            | Uniqlo Ultra Light Down Jacket      | Clothing    | $59.99  | 4     |
        When I navigate to first page using pagination
        Then products listed on page <1> should match given information
            | Product Name                   | Category    | Price    | Stars |
            | The Pragmatic Programmer       | Books       | $29.99   | 5     |
            | Wilson Pro Staff Tennis Racket | Sports      | $249.99  | 5     |
            | Samsung Smart Refrigerator     | Home        | $1799.99 | 5     |
            | Levi's 511 Slim Jeans          | Clothing    | $59.99   | 4     |
            | KitchenAid Stand Mixer         | Home        | $349.99  | 5     |
            | The 48 Laws of Power           | Books       | $23.99   | 4     |
            | Sony PlayStation 5             | Electronics | $499.99  | 5     |
            | Columbia Hiking Pants          | Clothing    | $69.99   | 4     |
            | Callaway Golf Set              | Sports      | $499.99  | 5     |
            | Dell XPS 13 Laptop             | Electronics | $1199.99 | 4     |
        When I navigate to last page using pagination
        Then products listed on page <5> should match given information
            | Product Name                  | Category | Price   | Stars |
            | The Lean Startup              | Books    | $19.99  | 4     |
            | Adidas Originals Hoodie       | Clothing | $74.99  | 4     |
            | Clean Code                    | Books    | $34.99  | 5     |
            | Panasonic Microwave Oven      | Home     | $129.99 | 4     |
            | Nike Mercurial Football Boots | Sports   | $199.99 | 5     |
            | Rich Dad Poor Dad             | Books    | $14.99  | 4     |
            | Mizuno Running Shorts         | Sports   | $34.99  | 4     |
            | Deep Work                     | Books    | $16.99  | 4     |
            | Nespresso Vertuo Coffee Maker | Home     | $179.99 | 4     |
            | Dyson V15 Detect Vacuum       | Home     | $699.99 | 5     |

Scenario: Verify product card details format
    Given I am on the product listing page
    When I navigate through all product pages
    Then each product card should display product name, price, category, and star rating in correct format
    And rating stars are visible and not modifiable by user