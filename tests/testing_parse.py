import unittest
from LED.parse import *

class Test_LED(unittest.TestCase):

    def test_read_file_local(self):
        file = "./data/test_data.txt"
        self.assertEqual(Parser.parse_files(file), 10)

    def test_read_file_network(self):
        file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        self.assertEqual(Parser.parse_files(file), 1000)


if __name__ == '__main__':
    unittest.main()

