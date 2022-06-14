import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.c=Customer(12345678912345, 'Marcos Aurelio')

    def test_Ccnumber(self):
        self.assertEqual(str(self.c.getCcNumber(), 12345678912345))











        



