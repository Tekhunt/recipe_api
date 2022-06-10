from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):

    def test_add(self):
        res = calc.add(3,4)
        self.assertEqual(res, 7)

    def test_subNum(self):
        res = calc.sub_num(10,5)
        self.assertEqual(res, 5)

        