from behave import given, then, when
from pages.product_listing_and_pagination.product_listing_pagination_page import ProductListingPaginationPage
from pages.start_page import StartPage

@given('I am on the product listing page')
def I_am_on_the_product_listing_page(context):
    context.page = ProductListingPaginationPage(context.driver).open()

@when('I count the number of products in each category')
def I_count_the_number_of_products_in_each_category(context):
    context.page.count_products_in_each_category()

@then('the product counts should match information from product data file')
def the_product_counts_should_match_information_from_product_data_file(context):
    context.page.verify_product_counts()