import unittest
import pytest
#from selenium import webdriver
from page.home.loginpage import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("sonybiswal093@gmail.com", "090093")
        result1 = self.lp.VerifyTitle()
        self.ts.mark(result1, " Title Verified ")
        result2 = self.lp.VerifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("sonybiswal093@gmail.com", "768")
        result = self.lp.VerifyLoginFailed()
        assert result == True