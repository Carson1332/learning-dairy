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


# Function: (Create New dataframe)
from typing import List
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns = ['student_id', 'age']
    df = pd.DataFrame(student_data, columns=columns)
    return df

# Function: (Create New dataframe)
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0] , players.shape[1]]
# Select Output Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    # OR return employees[:3]

# Located Data with column name
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]
    
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+
#create data automatically
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
# OR Dynamic Column 
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create bonus values
    bonus = employees['salary'] * 2
    # Insert at position 2 (third column)
    employees.insert(loc=2, column='bonus', value=bonus)
    return employees
# Delete Duplcate
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers
# subset: This is the column label or sequence of labels to consider for identifying duplicate rows. If not provided, it considers all columns in the DataFrame.
# keep: This argument determines which duplicate row to retain: 'first': (default) Drop duplicates except for the first occurrence.'last': Drop duplicates except for the last occurrence. False: Drop all duplicates.
# inplace: If set to True, the changes are made directly to the object without returning a new object. If set to False (default), a new object with duplicates dropped will be returned.
#delete missing column values 
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(
        axis=0,     # 0 for rows, 1 for columns
        how='any',  # 'any' or 'all'
        thresh=None,  # minimum number of non-NA values
        subset=None,  # columns to consider
        inplace=False  # False to return new DataFrame
    )

#Rename column
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students

# Argument Definition:

# mapper, index, columns: The dictionaries you can pass to rename index or columns. In our example, we use columns.

# axis: Can be either "index" or "columns". Determines whether you're renaming the index or the columns. By default, if you provide the columns argument, you're renaming columns.

# copy: If set to True, a new DataFrame is created. If False, the original DataFrame is modified.

# inplace: If set to True, the renaming will modify the DataFrame in place and nothing will be returned. If False, a new DataFrame with renamed columns will be returned without modifying the original DataFrame.

# level: For DataFrames with multi-level index, level from which the labels should be renamed.

# errors: If 'raise', an error is raised if you try to rename an item that doesn't exist. If set to 'ignore', any failure to rename items will be ignored.
