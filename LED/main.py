def main():
    """ Top level function which runs the program. """

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', ) # --input is positional argument/.
    args = parser.parse_args()
    filename = args.input

    grid_size = Parser.parse_files(filename) # send to parse_files function
