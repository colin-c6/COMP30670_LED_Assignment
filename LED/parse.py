import re
from urllib.request import urlopen

class Parser():
    def parse_files(files):

        if files.startswith('http'):
            with urlopen(files) as f:
                first_line = int(f.readline().strip()) #Using int() because it returns it as b'num' without it (binary numebr)

        else:
            with open(files) as f:
                first_line = int(f.readline().strip())

        return first_line
    
    
    
        def find_instructions(l):


            instruction1 = re.findall(".*(turn on|turn off|switch).*",l)
            instruction = ''.join(instruction1)
            coord = re.findall("\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*",l)
    
            first_coordinate = []
            first_x = int(coord[0][0])
            first_y = int(coord[0][1])
            first_coordinate += first_x,first_y
    
            second_coordinate = []
            second_x = int(coord[1][0])
            second_y = int(coord[1][1])
            second_coordinate += second_x,second_y


        return instruction, first_coordinate, second_coordinate

