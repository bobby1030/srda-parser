import json

import pandas as pd
from datetime import datetime


class ParsedTable:
    def __init__(self, header, tabledata):
        """
        Initialize the parsed table with header and table data
        """
        self.header = header
        self.tabledata = tabledata

    def to_frame(self):
        """
        Convert the parsed table to a pandas DataFrame
        """
        return pd.DataFrame(self.tabledata, columns=self.header)

    def to_variable_list(self):
        """
        Convert the parsed table to a list of Variable objects
        """
        variable_list = []
        for row in self.tabledata:
            variable = Variable()
            variable.q_id = row[0]
            variable.name = row[1]
            variable.field = row[2]
            variable.description = row[3]
            variable.values = row[4]
            variable.note = row[5]
            variable_list.append(variable)
        return variable_list


class Data:
    def __init__(self):
        self.title = None
        self.description = None
        self.date = None
        self.variables = []

    def to_json(self, filename=None):
        with open(filename, "w") as f:
            json.dump(self, f, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

class Variable:
    def __init__(self):
        self.q_id = None
        self.name = None
        self.field = None
        self.description = None
        self.values = None
        self.note = None

    def __repr__(self):
        return f"Variable({self.name}, {self.description})"


class Value:
    def __init__(self):
        pass
