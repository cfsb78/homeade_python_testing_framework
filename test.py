from testcase import TestCase
from wasrun import WasRun
from testresult import TestResult
from testsuite import TestSuite
from brokensetup import BrokenSetup

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")
        self.brokenTest = WasRun("testBrokenMethod")
        self.result = TestResult()
        self.brokenSetup = BrokenSetup("testMethod")

    def testTemplate(self):
        self.test.run(self.result)
        assert(self.test.log == "setUp|testMethod|tearDown|")

    def testResult(self):
        self.test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        self.brokenTest.run(self.result)
        assert("testBrokenMethod FAILED\n1 run, 1 failed" == self.result.summary())

    def testFailedResultFormat(self):
       self.result.startedTest()
       self.result.failedTest("failingTestName")
       assert("failingTestName FAILED\n1 run, 1 failed" == self.result.summary())


    def testSuite(self):
        suite = TestSuite()
        suite.addTest(WasRun("testMethod"))
        suite.addTest(WasRun("testBrokenMethod"))

        suite.run(self.result)
        assert("testBrokenMethod FAILED\n2 run, 1 failed" == self.result.summary())

    def testTearDownRunsAfterFailedTest(self):
        self.brokenTest.run(self.result)
        assert("setUp|testBrokenMethod|tearDown|" == self.brokenTest.log)

    def testSetUpFailIsReported(self):
        self.brokenSetup.run(self.result)
        assert("setUp FAILED\n0 run, 0 failed" == self.result.summary())

    def testAddingTestCaseToTestSuite(self):
        suite = TestSuite();
        suite.addTestCase(WasRun);
        suite.run(self.result);
        assert("testBrokenMethod FAILED\n2 run, 1 failed" == self.result.summary())


suite = TestSuite()
suite.addTestCase(TestCaseTest)
result = TestResult()
suite.run(result)
print result.summary()
