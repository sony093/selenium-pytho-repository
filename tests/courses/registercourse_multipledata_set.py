from page.courses.registercourse_page import RegisterCoursePage
from page.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1034", "12/20", "101", "34565"),
          ("Learn Python 3 from scratch", "2056", "11/22", "202", "67345"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.clickOnEnrollButton()
        time.sleep(1)
        self.courses.enterCreditCardInfo(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccZip)
        time.sleep(1)
        self.courses.clickAgreeToTerms()
        self.courses.clickEnrollSubmitButton()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']//img").click()
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

# self.driver.get("https://learn.letskodeit.com/courses")
# self.driver.find_element_by_link_text("All Courses").click()

# pytest -v -s tests/courses/registercourse_multipledata_set.py
