import unittest
from LED.parse import *

class Test_LED(unittest.TestCase):

    def test_read_file_local(self):
        '''function tests that HTTP:// files are correctly parsed in the parser.py script'''
        
        file = "./data/test_data.txt"
        line = "turn on 0,0 through 9,9"
        self.assertEqual(Parser.parse_files(file), 10,"Parser doesnt find the size of the grid correctly")
        self.assertEqual(Parser.find_instructions(line), ("turn on", [0,0], [9,9]), "Parser does not read the line correctly")

    def test_read_file_network(self):
        '''function tests that local files are correctly parsed in the parser.py script'''
        
        file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        self.assertEqual(Parser.parse_files(file), 1000, "Parser doesnt find the size of the grid correctly")

        line = "turn off 660,55 through 986,197"
        self.assertEqual(Parser.find_instructions(line), ("turn off", [660,55], [986,197]),"Parser does not read the line correctly")



if __name__ == '__main__':
    unittest.main()

