
from LED.parse import Parser
from urllib.request import urlopen
from LED.lightTester import LightTester
import argparse

def main():
    """ Top level function which runs the program. """

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', ) # --input is positional argument/.
    args = parser.parse_args()
    filename = args.input

    grid_size = Parser.parse_files(filename) # send to parse_files function
    
    #instigate an instance of the LightTester class
    grid1 = LightTester(grid_size)

    if filename.startswith('http'):
        with urlopen(filename) as fi:
            next(fi) #skips first line of file
            for line in fi:
                decoded_line = line.decode('utf-8') #decode the lines in the file       
                instruction, start_point, end_point = Parser.find_instructions(decoded_line)
                grid1.limits(instruction, start_point, end_point)
  
    else:
        with open(filename) as fi:
            next(fi)
            for line in fi:      
                instruction, start_point, end_point = Parser.find_instructions(line)
                grid1.limits(instruction, start_point, end_point)
                
    
    print("The number of lights turned on is:",grid1.count())