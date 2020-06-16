from excelimport.excelmapper import read_excel
from flask import Flask
app = Flask(__name__)

excel_dict = read_excel()
#print(excel_dict["General Information"])
@app.route('/')
def hello_world():
    text = ""
    for record in excel_dict.values():
        subtext = ""
        for row in record.iterrows():
            subtext = subtext + str(row) + "<br>"
        text = text + subtext + "<br>"
    return text


if __name__ == '__main__':
    app.run()