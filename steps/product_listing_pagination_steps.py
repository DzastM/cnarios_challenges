from behave import given, then, when
from pages.product_listing_and_pagination.product_listing_pagination_page import ProductListingPaginationPage
from pages.start_page import StartPage

@given('I am on the product listing page')
def I_am_on_the_product_listing_page(context):
    context.page = ProductListingPaginationPage(context.driver).open()

@when('I count the number of products in each category')
def I_count_the_number_of_products_in_each_category(context):
    context.page.count_products_in_each_category()

@when('I search for a product by name "{product_name}"')
def I_search_for_a_product_by_name(context, product_name):
    context.page.search_product_by_name(product_name)

@when('I identify the highest-rated products in each category')
def I_identify_the_highest_rated_products_in_each_category(context):
    context.page.find_products_by_rating(5)

@then('the product counts should match information from product data file')
def the_product_counts_should_match_information_from_product_data_file(context):
    context.page.verify_product_counts()

@then('I should find the product with correct data')
def I_should_find_the_product_with_correct_data(context):
    for row in context.table:
        product_name = row['Product Name']
        price = row['Price']
        category = row['Category']
        stars = row['Stars']
        context.page.verify_product_data(product_name, price, category, stars)

@then('product was found on page {page_number}')
def product_was_found_on_page(context, page_number):
    context.page.assert_page_number(int(page_number))

@then('the highest-rated products should match information given in table')
def the_highest_rated_products_should_match_information_given_in_table(context):
    for row in context.table:
        product_name = row['Product Name']
        context.page.assert_product_has_rating(product_name, 5)
        