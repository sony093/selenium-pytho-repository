from lib2to3.pgen2 import driver
from base.basepage import BasePage
from page.home.navigation_page import NavigationPage
import self
import utilities.customlogger as cl
import logging
import time


def def__init__():
    pass


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def__init__()
    # super().__init__(driver)
    self.driver = driver
    self.nav = NavigationPage(driver)

    def getTitle(self):
        return self.driver.title

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    # def VerifyLoginSuccessful(self):
    #     pass
    #
    # def VerifyLoginFailed(self, email):
    #     pass

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmailField(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPasswordField(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmailField(email)
        self.enterPasswordField(password)
        time.sleep(2)
        self.clickLoginButton()

    def VerifyLoginSuccessful(self):
        result = self.isElementPresent("navbar-current-user", locatorType="class") #Profile icon
        return result

    def VerifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", locatorType="xpath")
        return result

    def VerifyTitle(self):
        return self.VerifyPageTitle("Google")

    def logout(self):
        self.nav.navigateToUserSetting()
        self.elementClick(locator= "//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath")


# rc-anchor-error-msg-container
# //div[@class='alert alert-danger']