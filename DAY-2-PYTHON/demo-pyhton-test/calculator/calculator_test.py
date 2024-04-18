import unittest
import calculator
class TestSum(unittest.TestCase):
 
  def test_sum(self):    
    self.assertEqual(calculator.add(3, 2), 5)
 
  if __name__ =="__main__":
    unittest.main()