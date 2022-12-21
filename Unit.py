import unittest
from main import sum
from main import sub
from main import mul
from main import div


class test(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(sum(2,16), 18)
  def test_sub(self):
    self.assertEqual(sub(38,5), 33)
  def test_mul(self):
    self.assertEqual(mul(14,2), 28)
  def test_div(self):
    self.assertEqual(div(36,4), 9)
  def test_sum1(self):
    self.assertEqual(sum(10,21), 31)