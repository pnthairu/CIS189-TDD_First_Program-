import unittest
# importing main folder and function
from main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        # Testing if 3 years converted to months is 36
        self.assertEqual(camper_age_input.convert_to_months(3), 36)


if __name__ == '__main__':
    unittest.main()
