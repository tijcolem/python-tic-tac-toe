import unittest
import test.all_tests

print"\n\n*******Running Open Tests (Student & Teacher)********\n\n"

testSuite = test.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner(verbosity=2).run(testSuite)
