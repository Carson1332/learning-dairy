# Contents:
# Get the number of rows, columns, and elements in pandas.DataFrame
# - Display the number of rows, columns, etc.: df.info()
# - Get the number of rows and columns: df.shape
# - Get the number of rows: len(df)
# - Get the number of columns: len(df.columns)
# - Get the number of elements: df.size
# - Notes when setting an index
# Get the number of elements in pandas.Series
# - Get the number of elements: len(s), s.size


Function: (Create New dataframe)
from typing import List
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns = ['student_id', 'age']
    df = pd.DataFrame(student_data, columns=columns)
    return df

Function: (Create New dataframe)
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0] , players.shape[1]]


