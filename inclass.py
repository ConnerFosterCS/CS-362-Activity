# Connner Foster (932777502)
# cs362 section 001
# Code to calculate the average of a list
import calc
import unittest  

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  return x / y


class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(add(4, 2),6)
  def test2(self): self.assertEqual(sub(4, 2),2)
  def test3(self): self.assertEqual(mul(4, 2),8)
  def test4(self): self.assertEqual(sub(4, 2),2)


if __name__ == '__main__':
  unittest.main()