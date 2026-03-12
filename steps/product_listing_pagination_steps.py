from behave import given, then, when
from pages.product_listing_and_pagination.product_listing_pagination_page import ProductListingPaginationPage
from pages.start_page import StartPage
import random

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

@when('I click page {page_number}')
def I_click_page(context, page_number):
    context.page.click_page(int(page_number))

@when('I identify the most expensive products in each category')
def I_identify_the_most_expensive_products_in_each_category(context):
    context.page.find_most_expensive_products_in_each_category()

@when('I click "Next" button')
def I_click_next_button(context):
    context.page.click_next_page()

@when('I click "Previous" button')
def I_click_previous_button(context):
    context.page.click_previous_page()

@when('I navigate to first page using pagination')
def I_navigate_to_first_page_using_pagination(context):
    context.page.navigate_to_page(1)

@when('I navigate to last page using pagination')
def I_navigate_to_last_page_using_pagination(context):
    context.page.navigate_to_page(context.page.get_total_pages())

@when('I navigate through all product pages')
def I_navigate_through_all_product_pages(context):
    context.page.navigate_to_page(random.randint(1, context.page.get_total_pages())) # products will be checked on random page

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

@then('the most expensive products should match given information')
def the_most_expensive_products_should_match_given_information(context):
    for row in context.table:
        category = row['Category']
        product_name = row['Product Name']        
        context.page.assert_most_expensive_product(category, product_name)        

@then('products listed on page {page_number} should match given information')
def products_listed_on_page_should_match_given_information(context, page_number):
    for row in context.table:
        product_name = row['Product Name']
        category_name = row['Category']
        price = row['Price']
        stars = row['Stars']
        context.page.verify_product_data(product_name, price, category_name, stars)

@then('each product card should display product name, price, category, and star rating in correct format')
def each_product_card_should_display_product_name_price_category_and_star_rating_in_correct_format(context):
    context.page.verify_product_card_format()

@then('rating stars are visible and not modifiable by user')
def rating_stars_are_visible_and_not_modifiable_by_user(context):
    context.page.verify_rating_stars()