from django import forms

class Answer(forms.Form):
  BOOLEAN_CHOICES = (('1', 'Yes'), ('0', 'No'))
  isTrue = forms.ChoiceField(choices = BOOLEAN_CHOICES, widget = forms.RadioSelect)
