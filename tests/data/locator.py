from selenium.webdriver.common.by import By

class LoginPageLocator:
    USER_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    
class AddToCartLocator:
    ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_JACKET = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    ADD_T_SHIRT = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    ADD_CART = (By.ID, 'shopping_cart_container')
    TEXT_CART = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    
class ChechoutLocator:
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_INPUT = (By.ID, 'postal-code')
    TEXT_CHECKOUT = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    CONTINUE_BUTTON = (By.ID, 'continue')