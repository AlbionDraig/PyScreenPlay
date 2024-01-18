from scripts.actor import BrowseTheWeb, Open, SetText, Click, GetPageName, GetText

from data.locator import LoginPageLocator as LPL
from data.locator import AddToCartLocator as ATCL
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

from data.data import LoginPageData as LPD
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
    
