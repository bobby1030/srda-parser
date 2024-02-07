import sys

from .parser import extract_tables_from_docx, parse_docx_tables

# Usage example
file_path = sys.argv[1]
variable_table = extract_tables_from_docx(file_path)[0]
df = parse_docx_tables(variable_table)

df.to_csv("temp.csv", index=False)

print(df)
