from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class UploadBudgetForm(FlaskForm):
    file = FileField()