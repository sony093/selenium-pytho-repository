import logging
import time
from base.basepage import BasePage
import utilities.customlogger as cl


class RegisterCoursePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    # Locators
    _search_box = "search-courses"
    _search_course_icon = "search-course-button"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"  #JavaScript for beginners
    _all_courses = "//div[@class='course-listing-title']"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"  # xpath
    _cc_exp = "exp-date"  # name
    _cc_cvc = "cvc"  # name
    _postal_code = "postal"  # name
    _agree_to_terms = "agreed_to_terms_checkbox"  # id
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"
    _enroll_error_message = ""

    # element

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)
        self.elementClick(locator=self._search_course_icon)

    def selectCourseToEnroll(self, Fullcoursename):
        self.elementClick(locator=self._course.format(""), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNumber(self, num):
        self.switchToFrame(name="__privateStripeFrame8")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame9")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(name="__privateStripeFrame10")
        self.sendKeys(cvv, locator=self._cc_cvc, locatorType="name")
        self.switchToDefaultContent()

    def enterCardZip(self, zip):
        self.switchToFrame(name="__privateStripeFrame11")
        self.sendKeys(zip, locator=self._postal_code, locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTerms(self):
        self.elementClick(locator=self._agree_to_terms)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInfo(self, num, exp, cvv, zip):
        self.enterCardNumber(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterCardZip(zip)

    def enrollCourseInfo(self, num="", exp="", cvv="", zip=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInfo(num, exp, cvv, zip)
        time.sleep(3)
        self.clickAgreeToTerms()
        time.sleep(2)
        self.clickEnrollSubmitButton()
        time.sleep(2)

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Enroll Button")
        return not result
