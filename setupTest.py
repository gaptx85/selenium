import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		PATH = "/home/tester/Desktop/chromedriver_linux64/chromedriver"
		self.driver = webdriver.Chrome(PATH)

	def test_hit_python_homepage(self):
		driver = self.driver
		driver.get("http://www.google.com")
		self.assertIn("Google", driver.title)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()