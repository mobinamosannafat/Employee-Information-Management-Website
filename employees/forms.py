from django import forms
from . import models

class AddEmployee(forms.ModelForm): #EmployeeForm
    class Meta:
        model = models.Employee
        fields ="__all__"
        exclude = ()