from behave import given, then, when
from features.pages.product_purchasing import ProductPurchasingPage
from pages.start_page import StartPage

@given('I am on the homepage')
def I_am_on_the_homepage(context):
    context.page = StartPage(context.driver).open()

@given('I am on the product purchasing page')
def I_am_on_the_product_purchasing_page(context):
    context.page = ProductPurchasingPage(context.driver).open()

@when('I add products to the cart')
def I_add_products_to_cart(context):
    for row in context.table:
        product_name = row['Product Name']
        quantity = int(row['Quantity'])
        context.page.add_product_to_cart(product_name)

@when('I view the cart')
def I_view_the_cart(context):
    context.page.click_view_cart()
    

@then('the cart should contain')
def the_cart_should_contain(context):
    expected_items_list = {}
    for row in context.table:
        expected_items_list[row['Product Name']] = int(row['Quantity'])
    actual_items_list = context.page.get_item_name_and_quantity()
    for item in expected_items_list:
        assert item in actual_items_list, f"Expected item '{item}' not found in cart"

@given('I am on the Challenges page')
def I_am_on_the_challenges_page(context):
    context.page = StartPage(context.driver).open()
    context.page = context.page.click_option_button("Challenges")

@then('I should see the heading "{expected_heading}"')
def I_should_see_the_heading(context, expected_heading):
    actual_heading = context.page.get_heading_text()
    assert actual_heading == expected_heading, f"Expected heading '{expected_heading}', but got '{actual_heading}'"