import unittest
from tests.home.logintest import LoginTests
from tests.courses.registercourse_multipledata_set import RegisterMultipleCoursesTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterMultipleCoursesTests)

smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)


# pytest tests/home/test_suite.py