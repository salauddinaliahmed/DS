import sys
sys.path.insert(0,'/Users/salauddinali/Desktop/DS')
from mergesort import mergesort
import random

import unittest

class TestMerge(unittest.TestCase):
	def test_mergesort(self):
		for i in range(5):
			l = [ random.randint(-2356, 2554) for _ in range(1, random.randrange(2,12321))]
			# import pudb; pu.db
			self.assertEqual(mergesort(l), sorted(l))
