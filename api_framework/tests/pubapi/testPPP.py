from pubapiutils import Calls
from pubapiutils import Config
from pubapiutils import Utils
import httplib
import nose
from time import sleep
from unittest import TestCase


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.no_json = 'NoJSON'
        cls.calls = Calls()
        TestClass.config = Config()
        TestClass.utils = Utils()
        print('asd')

    def setUp(self):
        self.no_json = 'NoJSON'
        #self.calls = Calls()
        self.config = Config()
        self.utils = Utils()
        print('setup')
        sleep(1)

    def test_1(self):
        print('Test1')
        resp = self.calls.create_folder('test')
        print(resp.status_code)
        sleep(1)

    def test_2(self):
        print('Test2')
        sleep(1)

    def test_3(self):
        print('Test3')
        sleep(1)

    def tearDown(self):
        print('TearDown')