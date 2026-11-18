import unittest
from src.payment import charge
class Payment(unittest.TestCase):
    def test_new(self): self.assertTrue(charge(set(), 'a', 1))
    def test_duplicate(self):
        seen=set(); charge(seen,'a',1)
        self.assertFalse(charge(seen,'a',1))
    def test_boundary(self):
        with self.assertRaises(ValueError): charge(set(),'a',0)
    def test_error(self):
        with self.assertRaises(ValueError): charge(set(),'',1)
