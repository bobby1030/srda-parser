import sys
from pprint import pprint

from . import read_srda_docx

# Usage example
file_path = sys.argv[1]
pt = read_srda_docx(file_path)

pprint(pt.__dict__)