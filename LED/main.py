def main():
    """ Top level function which runs the program. """

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', ) # --input is positional argument/.
    args = parser.parse_args()
    filename = args.input

    grid_size = Parser.parse_files(filename) # send to parse_files function


    if filename.startswith('http'):
        with urlopen(filename) as fi:
            next(fi) #skips first line of file
            for line in fi:
                decoded_line = line.decode('utf-8') #decode the lines in the file       
                instruction, start_point, end_point = Parser.find_instructions(decoded_line)
  
    else:
        with open(filename) as fi:
            next(fi)
            for line in fi:      
                instruction, start_point, end_point = Parser.find_instructions(line)