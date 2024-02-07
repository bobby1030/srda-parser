import pandas as pd
from docx import Document


def extract_tables_from_docx(file_path):
    doc = Document(file_path)
    tables = doc.tables
    return tables


def parse_docx_tables(table):
    table_data = []

    # construct header from the first row
    header_cells = table.rows[0].cells
    header = []
    for cellidx in range(len(header_cells)):
        if cellidx > 0 and header_cells[cellidx].text == header_cells[cellidx - 1].text:
            pass  # left merge cells with duplicated header
        else:
            header.append(header_cells[cellidx].text)

    # init a variable to store running common title
    common_title = (None, None)  # (q_id, common_title)

    # loop through rows
    for row in table.rows[1:]:
        row_data = []

        # loop through cells within row
        for cell in row.cells:
            if len(row_data) > 0 and cell.text == row_data[-1]:
                pass  # left merge cells with duplicated content
            else:
                row_data.append(cell.text)

        # truncate row_data to match header length
        row_data = row_data[: len(header)]

        # identify rows that served as common title for following rows
        # and rollover the title to the next row
        if row_data[0] != "" and len(row_data) > 1 and len(row_data) < len(header) - 1:
            # is a common title row
            common_title = (row_data[0], row_data[1])  # (q_id, common_title)
        else:
            # is not a common title row
            description_idx = header.index(
                "變項說明"
            )  # get the position of variable description
            if row_data[0] == common_title[0]:
                # same q_id as common title
                row_data[description_idx] = common_title[1] + row_data[description_idx]

            # skip rows that served as separators
            if len(row_data) > 1:
                table_data.append(row_data)

    df = pd.DataFrame(table_data, columns=header)
    return df
