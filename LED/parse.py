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