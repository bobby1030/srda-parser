import pandas as pd
from datetime import datetime


class ParsedTable:
    def __init__(self, header, tabledata):
        """
        Initialize the parsed table with header and table data
        """
        self.header = header
        self.tabledata = tabledata

        self.normalize_header()

    def to_frame(self):
        """
        Convert the parsed table to a pandas DataFrame
        """
        return pd.DataFrame(self.tabledata, columns=self.header)
    
    def normalize_header(self):
        """
        Normalize the header by:
        1. mapping chinese header string to english header
        """
        header_dict = {
            "題號": "q_id",
            "變項名稱": "name",
            "卡數/欄位定義": "field",
            "變項說明": "description",
            "選項數值說明": "values",
            "備註": "note",
        }
        self.header = [header_dict[h] for h in self.header]


class Data:
    def __init__(self):
        self.title = None
        self.description = None
        self.date = None
        self.variables = []


class Variable:
    def __init__(self):
        self.q_id = None
        self.name = None
        self.field = None
        self.description = None
        self.values = []
        self.note = None


class Value:
    def __init__(self):
        pass
