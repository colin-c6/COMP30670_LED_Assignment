import re
from urllib.request import urlopen

class Parser():
    ''' Class that contains functions to parse files'''
    
    def parse_files(files):
        ''' function to parse a local or network file and return the first line which contains an int representing the grid size'''
        
        if files.startswith('http'):
            with urlopen(files) as f:
                first_line = int(f.readline().strip()) #Using int() because it returns it as b'num' without it (binary numebr)

        else:
            with open(files) as f:
                first_line = int(f.readline().strip())

        return first_line
    
    
    
    def find_instructions(line):
        ''' function parses each recieved line into its command, start coordinates an end coordinates'''

        #finding the instruction and then converting it to a string
        instruction1 = re.findall(".*(turn on|turn off|switch).*",line)
        instruction = ''.join(instruction1)
        coordinates = re.findall("\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*",line)
    
        start_coordinate = []
        x1 = int(coordinates[0][0])
        y1 = int(coordinates[0][1])
        start_coordinate += x1,y1
    
        end_coordinate = []
        x2 = int(coordinates[1][0])
        y2 = int(coordinates[1][1])
        end_coordinate += x2,y2


        return instruction, start_coordinate, end_coordinate

