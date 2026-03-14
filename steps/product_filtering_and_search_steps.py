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

@then('only products from "{category}" category should be displayed')
def only_products_from_category_should_be_displayed(context, category):
    context.page.verify_product_category(category)