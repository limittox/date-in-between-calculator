import unittest
from modules import dateDiff
from modules.date import date

class TestDateDiff(unittest.TestCase):
	def test_dateDiff(self):
		self.assertEqual(dateDiff.calcDateDiff(date(2,6,1983), date(22,6,1983)), 19)
		# Day difference is actually 173 and not 179 as given
		self.assertEqual(dateDiff.calcDateDiff(date(4,7,1984), date(25,12,1984)), 173)
		self.assertEqual(dateDiff.calcDateDiff(date(3,1,1989), date(3,8,1983)), 1979)
		self.assertEqual(dateDiff.calcDateDiff(date(1,1,2012), date(28,2,2012)), 57)
		self.assertEqual(dateDiff.calcDateDiff(date(1,1,2012), date(1,3,2012)), 59)
		self.assertEqual(dateDiff.calcDateDiff(date(30,6,2011), date(30,6,2012)), 365)
		self.assertEqual(dateDiff.calcDateDiff(date(1,1,2011), date(8,8,2012)), 584)
		self.assertEqual(dateDiff.calcDateDiff(date(15,5,1994), date(31,8,2019)), 9238)
		self.assertEqual(dateDiff.calcDateDiff(date(24,3,1999), date(4,2,2018)), 6891)
		self.assertEqual(dateDiff.calcDateDiff(date(24,6,1999), date(4,8,2018)), 6980)
		self.assertEqual(dateDiff.calcDateDiff(date(24,5,1995), date(15,12,2018)), 8605)
		self.assertEqual(dateDiff.calcDateDiff(date(24,8,1994), date(15,12,2019)), 9243)
		self.assertEqual(dateDiff.calcDateDiff(date(15,12,2019), date(24,8,1994)), 9243)
		self.assertEqual(dateDiff.calcDateDiff(date(15,5,2019), date(24,10,1994)), 8968)
		self.assertEqual(dateDiff.calcDateDiff(date(24,11,1994), date(15,8,2019)), 9029)


if __name__ == '__main__':
	unittest.main()