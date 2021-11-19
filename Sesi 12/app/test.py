# from fractions import Fraction
# import unittest

# from my_sum import sum


# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)

# if __name__ == '__main__':
#     unittest.main()

#/////////////////

# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)

#     def test_list_fraction(self):
#         """
#         Test that it can sum a list of fractions
#         """
#         data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
#         result = sum(data)
#         self.assertEqual(result, 1)

# if __name__ == '__main__':
#     unittest.main()

#///////////////

from my_app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions