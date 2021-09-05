from flask import Blueprint
from flask import render_template
from .forms import UploadBudgetForm
from .calculate_budget import calculate_budget

mainpage_bp = Blueprint('uploadBudgetDataPage', __name__)
home_bp = Blueprint('uploadBudgetData', __name__)
home_bp.register_blueprint(mainpage_bp)

@home_bp.route('/', methods=['GET'])
def uploadBudgetDataPage():
    form = UploadBudgetForm(csrf_enabled=False)
    return render_template('uploadBudgetDataPage.html', form = form)

@mainpage_bp.route('/uploadBudgetData', methods=['POST'])
def uploadBudgetData():
    form = UploadBudgetForm(csrf_enabled=False)
    file = form.file
    data = calculate_budget(file.data)
    data1 = []
    data2 = []
    for i in data:
        data1.append(i[1])
        data2.append(i[2])
    return render_template('budgetResult.html', data1 = data1, data2 = data2)