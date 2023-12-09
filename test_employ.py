import unittest
from unittest.mock import patch
from Employ import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass') 

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('Andrews', 'Osei', 50000)
        self.emp_2 = Employee('Kyere', 'Dwomoh', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'AndrewsOsei@email.com')
        self.assertEqual(self.emp_2.email, 'KyereDwomoh@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'JohnOsei@email.com')
        self.assertEqual(self.emp_2.email, 'JaneDwomoh@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Andrews Osei')
        self.assertEqual(self.emp_2.fullname, 'Kyere Dwomoh')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Osei')
        self.assertEqual(self.emp_2.fullname, 'Jane Dwomoh')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raises()
        self.emp_2.apply_raises()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('Employ.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Osei/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Dwomoh/June')
            self.assertEqual(schedule,'Bad Response!')

if __name__ == '__main__':
    unittest.main()