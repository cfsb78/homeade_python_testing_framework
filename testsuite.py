from testresult import TestResult
from optparse import OptionParser
import inspect
class TestSuite:
    def __init__(self):
        self.tests = []
        self.log = ""
    def addTest(self, test):
        self.tests.append(test)

    def addTestCase(self, testCase):
        parser = OptionParser()
        for name,method in inspect.getmembers(testCase, predicate=inspect.ismethod):
            if name.startswith("test"):
                self.addTest(testCase(name))

    def run(self, result):
        for test in self.tests:
            test.run(result)
