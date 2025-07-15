
from playwright.sync_api import *


def get_users(playwright:Playwright):
    api_context=playwright.request.new_context(
    base_url= "https://dummyjson.com"
    )
    response = api_context.get("/users/1")
    response_product=api_context.get("/products")
    #print(response_product.json())
    #product_data = response_product.json()
    user_data=response.json()
    assert "firstName" in user_data
    assert user_data["firstName"] == "Emily"
    #assert "reviewerEmail" in product_data
    #assert user_data["city"] == "Washington"

    api_context.dispose()