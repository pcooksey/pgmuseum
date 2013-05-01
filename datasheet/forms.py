from django import forms
from datasheet.models import *

class BasicForm(forms.ModelForm):
  class Meta:
    model = Basic
    exclude = ("createdBy",)

class ClusterForm(forms.ModelForm):
  class Meta:
    model = ClusterInfo
    exclude = ("basic",)

class ExplorationForm(forms.ModelForm):
  class Meta:
    model = ExplorationTime
	
class CountForm(forms.ModelForm):
  class Meta:
    model = CountTime
	
class WeatherForm(forms.ModelForm):
  class Meta:
    model = Weather
	
class ObservedForm(forms.ModelForm):
  class Meta:
    model = Observed
	
class ExplorationForm(forms.ModelForm):
  class Meta:
    model = ExplorationTime