import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    text = 'response.ok = True'
    status_code = 200
    elapsed = 100
    ok = True

    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    text = 'response.ok = False'
    status_code = 400
    elapsed = 100
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('John', 'Smith', 40000)
        self.employee2 = Employee('Neo', 'Cordic', 52000)

    def test_email(self):
        self.assertEqual(self.employee1.email.lower(), 'john.smith@email.com')
        self.assertEqual(self.employee2.email.lower(), 'neo.cordic@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname.lower(), 'john smith')
        self.assertEqual(self.employee2.fullname.lower(), 'neo cordic')

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 42000)
        self.assertEqual(self.employee1.pay, 42000.00)
        self.employee2.apply_raise()
        self.assertEqual(self.employee2.pay, 54600)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mocker):
        mocker.side_effect = MockTestTrue
        self.assertEqual(self.employee1.monthly_schedule('April'), 'response.ok = True')
        self.assertEqual(self.employee2.monthly_schedule('May'), 'response.ok = True')

        mocker.side_effect = MockTestFalse
        self.assertEqual(self.employee1.monthly_schedule('February'), 'Bad Response!')
        self.assertEqual(self.employee2.monthly_schedule('March'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()