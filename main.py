from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/', metods=['GET'])
def uploadBudgetDataPage():
    return render_template('uploadBudgetDataPage.html')

@app.route('/uploadBudgetData', metods=['POST'])
def uploadBudgetData(BudgetData):
    return render_template('budgetResult.html')

if __name__ == '__main__':
    app.run()
