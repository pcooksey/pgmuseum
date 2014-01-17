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
  def __init__(self, *args, **kwargs):
	super(ClusterForm, self).__init__(*args, **kwargs)
	self.fields['tree_ID'].required = False
  def clean_tree_ID(self):
	data = self.cleaned_data['tree_ID']
	if not data:
		return "N/A"
	return self.cleaned_data['tree_ID']

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
  def __init__(self, *args, **kwargs):
	super(ObservedForm, self).__init__(*args, **kwargs)
	self.fields['loners'].required = False
	self.fields['sunners'].required = False
	self.fields['fliers'].required = False
	self.fields['grounders'].required = False
	self.fields['dead'].required = False
	self.fields['mating'].required = False
	self.fields['observed_total'].required = False
  def clean_loners(self):
	data = self.cleaned_data['loners']
	if not data:
		return 0
	return self.cleaned_data['loners']
  def clean_sunners(self):
	data = self.cleaned_data['sunners']
	if not data:
		return 0
	return self.cleaned_data['sunners']
  def clean_fliers(self):
	data = self.cleaned_data['fliers']
	if not data:
		return 0
	return self.cleaned_data['fliers']
  def clean_grounders(self):
	data = self.cleaned_data['grounders']
	if not data:
		return 0
	return self.cleaned_data['grounders']
  def clean_dead(self):
	data = self.cleaned_data['dead']
	if not data:
		return 0
	return self.cleaned_data['dead']
  def clean_mating(self):
	data = self.cleaned_data['mating']
	if not data:
		return 0
	return self.cleaned_data['mating']
  def clean_observed_total(self):
	data = self.cleaned_data['observed_total']
	if not data:
		return 0
	return self.cleaned_data['observed_total']
	
class ExplorationForm(forms.ModelForm):
  class Meta:
    model = ExplorationTime

class NotesForm(forms.ModelForm):
  class Meta:
    model = Note
  def __init__(self, *args, **kwargs):
	super(NotesForm, self).__init__(*args, **kwargs)
	self.fields['waterNotes'].required = False
	self.fields['nectarNotes'].required = False
	self.fields['additionalNotes'].required = False
	
class FlowerForm(forms.ModelForm):
  class Meta:
    model = Flowers
    exclude = ("basic",)