from django import forms
from datasheet.models import *

class SelectForm(forms.Form):
	sites = forms.ModelMultipleChoiceField(queryset=SiteName.objects.all(),label='Select all that apply',required=True,widget=forms.CheckboxSelectMultiple(attrs={"checked":""})) 