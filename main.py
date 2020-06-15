from excelimport.excelmapper import read_excel
from flask import Flask
app = Flask(__name__)

excel_dict = read_excel()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()