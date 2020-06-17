from excelimport.excelmapper import read_excel
from creator.creator import create_exams
from flask import Flask
app = Flask(__name__)

excel_dict = read_excel()


@app.route('/')
def hello_world():
    text = ""
    for record in excel_dict.values():
        subtext = ""
        for row in record.iterrows():
            subtext = subtext + str(row) + "<br>"
        text = text + subtext + "<br>"
    return text


@app.route('/1')
def hello_world1():
    exams = create_exams(10, excel_dict)
    text = ""
    for exam in exams:
        subtext = ""
        for row in exam.values():
            subtext = subtext + str(row) + "<br>"
        text = text + subtext + "<br>"
    return text


if __name__ == '__main__':
    app.run()
