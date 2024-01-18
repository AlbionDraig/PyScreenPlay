from scripts.actor import Actor, BrowseTheWeb, Open, SetText, Click, GetPageName
from data.data import LoginPageData as LPD
from data.locator import LoginPageLocator as LPL

def test_login_scenario():
    actor = Actor(name="Sebastian")
    # Define las tareas e interacciones
    login_scenario = (
        BrowseTheWeb(),
        Open(url=LPD.URL),
        SetText(value=LPD.USER, element=LPL.USER_INPUT),
        SetText(value=LPD.PASSWORD, element=LPL.PASSWORD_INPUT),
        Click(element=LPL.LOGIN_BUTTON)
    )

    # Ejecuta el escenario
    for task in login_scenario:
        task.perform_as(actor)

    # Verifica el resultado
    assert GetPageName().perform_as(actor) == LPD.PAGE_NAME

if __name__ == "__main__":
    test_login_scenario()
