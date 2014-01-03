from testresult import TestResult
import traceback
class TestCase:

    def __init__(self, name):
        self.name = name

    def run(self, result):
        try:
            self.setUp()

            try:
                result.startedTest()
                method = getattr(self, self.name)
                method()
            except:
                result.failedTest(self.name)
                traceback.print_exc()

        except:
            result.failedSetUp()
            traceback.print_exc()

        finally:
            self.tearDown()



    def setUp(self):
        pass

    def tearDown(self):
        pass


