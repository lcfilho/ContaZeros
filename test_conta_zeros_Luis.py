import unittest
import conta_zeros_Luis

class Test_conta_zeros(unittest.TestCase):
    def test_conta_zeros(self):
        self.assertEqual(conta_zeros_Luis.conta_zeros('123 0000 1230'),(4))
    def test_conta_zeros_1(self):
        self.assertEqual(conta_zeros_Luis.conta_zeros('123 00 1200'),2)
    def test_conta_zeros_2(self):
        self.assertEqual(conta_zeros_Luis.conta_zeros('123 00 0002'),3)
    def test_conta_zeros_3(self):
        self.assertEqual(conta_zeros_Luis.conta_zeros('asdk23000 wadke0'),3)
    def test_conta_zeros_4(self):
        self.assertEqual(conta_zeros_Luis.conta_zeros('1230 0000'),4)
    def test_conta_zeros_5(self):
        self.assertFalse(conta_zeros_Luis.conta_zeros(''),())

if __name__ == "__main__":
    unittest.main()
