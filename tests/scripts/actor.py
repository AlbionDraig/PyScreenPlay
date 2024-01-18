from selenium import webdriver

class Actor:
    def __init__(self, name):
        self.name = name
        self.browser = None

    def using_browser(self, browser):
        self.browser = browser

class Task:
    def perform_as(self, actor):
        pass

class BrowseTheWeb(Task):
    def perform_as(self, actor):
        actor.using_browser(webdriver.Chrome())
        actor.browser.maximize_window()

class Open(Task):
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        actor.browser.get(self.url)

class SetText(Task):
    def __init__(self, value, element):
        self.value = value
        self.element = element

    def perform_as(self, actor):
        actor.browser.find_element(*self.element).send_keys(self.value)

class Click(Task):
    def __init__(self, element):
        self.element  = element

    def perform_as(self, actor):
        actor.browser.find_element(*self.element).click()

class GetPageName(Task):
    def perform_as(self, actor):
        return actor.browser.title

class GetText(Task):
    def __init__(self, element):
        self.element = element

    def perform_as(self, actor):
        return actor.browser.find_element(*self.element).text
