import sys

from .parser import extract_tables_from_docx, parse_docx_table

# Usage example
file_path = sys.argv[1]
variable_table = extract_tables_from_docx(file_path)[0]
pt = parse_docx_table(variable_table)

pt.to_frame().to_csv("temp.csv", index=False)
