from page.courses.registercourse_page import RegisterCoursePage
from utilities.teststatus import TestStatus
from page.home.navigation_page import NavigationPage
import unittest
import pytest
from ddt import ddt, data, unpack
import time
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    # def setUp(self):
    #     self.driver.find_element_by_link_text("All Courses").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\Abinash\\PycharmProjects\\RegisterCourse\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.clickOnEnrollButton()
        time.sleep(1)
        self.courses.enterCreditCardInfo(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccZip)
        time.sleep(1)
        self.courses.clickAgreeToTerms()
        time.sleep(1)
        self.courses.clickEnrollSubmitButton()
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']//img").click()
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")





# self.driver.get("https://learn.letskodeit.com/courses")
# self.driver.find_element_by_link_text("All Courses").click()
# pytest -v -s tests/courses/registercourse_csvdata.py
