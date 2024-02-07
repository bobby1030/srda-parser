import sys

from . import read_srda_docx

input_file = sys.argv[1]
output_file = sys.argv[2] or input_file.replace(".docx", ".json")

# Parse the input using the srda-parser
parsed_data = read_srda_docx(input_file)

# Write the parsed data to the output file
parsed_data.to_json(output_file)
