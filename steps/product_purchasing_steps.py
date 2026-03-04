from behave import given, then, when
from pages.product_purchasing_flow.product_purchasing_page import ProductPurchasingPage
from pages.start_page import StartPage

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
    context.page = context.page.click_view_cart()

@when('I increase the quantity of "{product_name}" to {expected_quantity}')
def I_increase_the_quantity_of_product(context, product_name, expected_quantity):
    context.page.update_product_quantity(product_name, int(expected_quantity))   

@when('I decrease the quantity of "{product_name}" to {expected_quantity}')
def I_decrease_the_quantity_of_product(context, product_name, expected_quantity):
    context.page.update_product_quantity(product_name, int(expected_quantity))   

@when('I proceed to address')
def I_proceed_to_address(context):
    context.page.click_proceed_to_address()

@then('"Proceed to Payment" button should be disabled')
def proceed_to_payment_button_should_be_disabled(context):
    context.page.assert_proceed_to_payment_button_disabled()

@then('the cart should contain')
def the_cart_should_contain(context):
    expected_items_list = {}
    for row in context.table:
        expected_items_list[row['Product Name']] = int(row['Quantity'])
    actual_items_list = context.page.get_item_name_and_quantity()
    for item in expected_items_list:
        assert item in actual_items_list, f"Expected item '{item}' not found in cart"

@then('total price should be "{expected_total_price}"')
def total_price_should_be(context, expected_total_price):
    actual_total_price = context.page.get_total_price()
    assert actual_total_price == expected_total_price, f"Expected total price '{expected_total_price}', but got '{actual_total_price}'"

@then('the cart should be empty')
def the_cart_should_be_empty(context):
    context.page.assert_if_cart_is_empty()