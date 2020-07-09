import pytest
import unittest
from utilities.teststatus import TestStatus
from page.courses.registercourse_page import RegisterCoursePage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_InvalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("Java Script for Beginners")
        self.courses.clickOnEnrollButton()
        self.courses.enterCreditCardInfo(num="1234 567 8901 2345", exp="02/23", cvv="191", zip="987654")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_InvalidEnrollment", result, "Enrollment Verification Failed")