from behave import given, then, when
from features.pages.product_purchasing import ProductPurchasingPage
from pages.start_page import StartPage

@given('I am on the homepage')
def I_am_on_the_homepage(context):
    context.page = StartPage(context.driver).open()

@given('I am on the product purchasing page')
def I_am_on_the_product_purchasing_page(context):
    context.page = ProductPurchasingPage(context.driver).open()

@when('I add "{product_name}" to the cart')
def I_add_product_to_cart(context, product_name):
    context.page.add_product_to_cart(product_name)

@when('I view the cart')
def I_view_the_cart(context):
    context.page.click_view_cart()
    context.cart_items = context.page.get_cart_items()





@given('I am on the Challenges page')
def I_am_on_the_challenges_page(context):
    context.page = StartPage(context.driver).open()
    context.page = context.page.click_option_button("Challenges")

@then('I should see the heading "{expected_heading}"')
def I_should_see_the_heading(context, expected_heading):
    actual_heading = context.page.get_heading_text()
    assert actual_heading == expected_heading, f"Expected heading '{expected_heading}', but got '{actual_heading}'"