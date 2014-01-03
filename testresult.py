class TestResult:

    def __init__(self):
        self.runCount = 0
        self.setupFailed = False
        self.failedTests = []
    def startedTest(self):
        self.runCount = self.runCount + 1


    def failedTest(self,failedTestName):
        self.failedTests.append(failedTestName)

    def failedSetUp(self):
        self.setupFailed = True

    def summary(self):
        msg = ""
        if self.setupFailed:
            msg += "setUp FAILED\n"

        for failedTest in self.failedTests:
           msg = msg + failedTest + " FAILED\n"
        msg += "%d run, %d failed" % (self.runCount , len(self.failedTests))
        return msg


