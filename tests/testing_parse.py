import unittest
from LED.parse import *

class Test_LED(unittest.TestCase):

    def test_read_file_local(self):
        file = "./data/test_data.txt"
        line = "turn on 0,0 through 9,9"
        self.assertEqual(Parser.parse_files(file), 10)
        self.assertEqual(Parser.find_instructions(line), ("turn on", [0,0], [9,9]))

    def test_read_file_network(self):
        file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        self.assertEqual(Parser.parse_files(file), 1000)

        line = "turn off 660,55 through 986,197"
        self.assertEqual(Parser.find_instructions(line), ("turn off", [660,55], [986,197]))



if __name__ == '__main__':
    unittest.main()

