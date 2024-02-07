#!/bin/bash

# Check if the input file exists
if [ ! -f "$1" ]; then
  echo "Input file does not exist"
  exit 1
fi

# Check if LibreOffice is installed
if ! command -v soffice &> /dev/null; then
  echo "LibreOffice is not installed"
  exit 1
fi

# Convert .doc to .docx
soffice --headless --convert-to docx "$1"

# Check if the conversion was successful
if [ $? -eq 0 ]; then
  echo "Conversion completed successfully"
else
  echo "Conversion failed"
fi
