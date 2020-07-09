from lib2to3.pgen2 import driver
from base.basepage import BasePage
import self
import utilities.customlogger as cl
import logging


def def__init__():
    pass


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def__init__()
    # super().__init__(driver)
    self.driver = driver

    def getTitle(self):
        return self.driver.title

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_setting_icon = "//div[@id='navbar']//span[text()='navbar-current-user']"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="Link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="Link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="Link")

    def navigateToUserSetting(self):
        self.elementClick(locator=self._user_setting_icon, locatorType="xpath")



    # rc-anchor-error-msg-container
    # //div[@class='alert alert-danger']
