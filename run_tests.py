import unittest
import test.all_tests


testSuite = test.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner(verbosity=2).run(testSuite)
print"\n\n*******Ran Open Tests (Student & Teacher)********\n\n"
