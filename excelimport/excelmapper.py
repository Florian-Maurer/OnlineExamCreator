import pandas as pd


# Get the number of sheets
def get_number_of_sheets():
    xl = pd.ExcelFile(r'..\TestExam.xlsx')
    number_sheets = len(xl.sheet_names)
    return number_sheets


# Return the specified excel file as dictionary
def read_excel():
    number = get_number_of_sheets()
    sheets = {}
    sheets["General Information"] = pd.read_excel(r'..\TestExam.xlsx', sheet_name='General Information')
    for index in range(1, number):

        df = pd.read_excel(r'..\TestExam.xlsx', sheet_name='Task ' + str(index))
        sheets['Task ' + str(index)] = df
    return sheets
