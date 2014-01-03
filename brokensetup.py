from testcase import TestCase


class BrokenSetup(TestCase):

    def setUp(self):
        raise Exception

    def testMethod(self):
        pass
