from testcase import TestCase


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ""

    def testMethod(self):
        self.log += "testMethod|"

    def testBrokenMethod(self):
        self.log += "testBrokenMethod|"
        raise Exception


    def setUp(self):
        self.log += "setUp|"

    def tearDown(self):
        self.log += "tearDown|"
