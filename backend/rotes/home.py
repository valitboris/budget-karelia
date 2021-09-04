from flask import Blueprint
from flask import render_template
from .forms import UploadBudgetForm

mainpage_bp = Blueprint('uploadBudgetDataPage', __name__)
home_bp = Blueprint('uploadBudgetData', __name__)

@home_bp.route('/', methods=['GET'])
def uploadBudgetDataPage():
    form = UploadBudgetForm(csrf_enabled=False)
    return render_template('uploadBudgetDataPage.html', form = form)

@mainpage_bp.route('/uploadBudgetData', methods=['POST'])
def uploadBudgetData():
    form = UploadBudgetForm(csrf_enabled=False)
    #exelTable = request.files['budgetExel.xls']
    #viewModel = calculate_budget(exelTable)
    return render_template('budgetResult.html')