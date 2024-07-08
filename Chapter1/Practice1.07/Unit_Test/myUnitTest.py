from unittest import TestCase, main


class severalTests(TestCase) :
	def test_firstCase(self) :
		self.assertEqual("I am " + "very" + " happy!", "I am very happy!")

	def test_secondCase(self) :
		self.assertTrue(4 * 8 == 2 ** 5)

	def test_thirdCase(self) :
		self.assertLess(10000 - 9999, 3)

	def test_forthCase(self) :
		self.assertIn(26, [13, 26, 39, 52])

	def test_fifthCase(self) :
		self.assertIsInstance((1, 3, 5), tuple)


if __name__ == "__main__" :
	main()
