from django import forms
from datasheet.models import *

class BasicForm(forms.ModelForm):
  class Meta:
	model = Basic
	exclude = ("createdBy","exploration_time","butterflies_observed","weather","count_time", "notes")
	

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

class NotesForm(forms.ModelForm):
  class Meta:
    model = Notes
	
class FlowerForm(forms.ModelForm):
  class Meta:
    model = Flowers
    exclude = ("basic",)