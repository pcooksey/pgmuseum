from django import forms
from datasheet.models import Basic, ClusterInfo

class BasicForm(forms.ModelForm):
  class Meta:
    model = Basic
    exclude = ("createdBy",)

class ClusterForm(forms.ModelForm):
  class Meta:
    model = ClusterInfo
    exclude = ("basic",)
