from django import forms


class CompanyForm(forms.Form):
    name = forms.CharField()
