from behave import given, then, when
from pages.product_filtering_and_search.product_filtering_and_search_page import ProductFilteringAndSearchPage
from pages.start_page import StartPage
import random

@given('I am on the product filtering page')
def i_am_on_the_product_filtering_page(context):
    context.page = ProductFilteringAndSearchPage(context.driver)
    context.page.open()

@when('I filter products by category "{category}"')
def i_filter_products_by_category(context, category):
    context.page.filter_by_category(category)

@when('I filter products with price range "{min_price}" to "{max_price}"')
def i_filter_products_with_price_range(context, min_price, max_price):
    context.page.set_price_minimum(min_price)
    context.page.set_price_maximum(max_price)

@then('only products from "{category}" category should be displayed')
def only_products_from_category_should_be_displayed(context, category):
    context.page.verify_product_category(category)

@then('only products priced between "{min_price}" and "{max_price}" should be displayed')
def only_products_priced_between_should_be_displayed(context, min_price, max_price):
    context.page.verify_product_price_range(min_price, max_price)