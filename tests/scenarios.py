from scripts.actor import BrowseTheWeb, Open, SetText, Click, GetPageName, GetText

from data.locator import LoginPageLocator as LPL
from data.data import LoginPageData as LPD
def login(actor):
    # Define tasks
    scenario = (
        BrowseTheWeb(),
        Open(url=LPD.URL),
        SetText(value=LPD.USER, element=LPL.USER_INPUT),
        SetText(value=LPD.PASSWORD, element=LPL.PASSWORD_INPUT),
        Click(element=LPL.LOGIN_BUTTON)
    )
    # Execute scenario
    for task in scenario:
        task.perform_as(actor)
    # Verify result
    assert GetPageName().perform_as(actor) == LPD.PAGE_NAME

from data.locator import AddToCartLocator as ATCL
from data.data import AddToCartData as ATCD
def adding_car(actor):
    # Define tasks
    scenario = (
        Click(element=ATCL.ADD_BACKPACK),
        Click(element=ATCL.ADD_JACKET),
        Click(element=ATCL.ADD_T_SHIRT),
        Click(element=ATCL.ADD_CART)
    )
    # Execute scenario
    for task in scenario:
        task.perform_as(actor)
    # Verify result
    assert GetText(element=ATCL.TEXT_CART).perform_as(actor) == ATCD.TEXT_CART
    
from data.locator import ChechoutLocator as COL
from data.data import CheckoutData as COD
def checkout(actor):
    # Define tasks
    scenario = (
        Click(element=COL.CHECKOUT_BUTTON),
        SetText(value=COD.FIRST_NAME, element=COL.FIRST_NAME_INPUT),
        SetText(value=COD.LAST_NAME, element=COL.LAST_NAME_INPUT),
        SetText(value=COD.ZIP, element=COL.ZIP_INPUT),
        Click(element=COL.CONTINUE_BUTTON)
    )
    # Execute scenario
    for task in scenario:
        task.perform_as(actor)
    # Verify result
    assert GetText(element=COL.TEXT_CHECKOUT).perform_as(actor) == COD.TEXT_CHECKOUT
    
