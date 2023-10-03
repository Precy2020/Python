from unittest import TestCase
from mr_femi import sum_alphanumeric


class SumAlphanumeric(TestCase):

    def test_that_string_numbers_can_be_summed(self):
        self.assertEqual(6, sum_alphanumeric.sum_string_numeric("abc123"))
        self.assertEqual(8, sum_alphanumeric.sum_string_numeric("bod1o7d-5"))
        self.assertEqual(12, sum_alphanumeric.sum_string_numeric("go3kil9"))
