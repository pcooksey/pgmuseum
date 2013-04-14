from django import forms
from donor.models import Donor, Donation

class DonorForm(forms.ModelForm):
  class Meta:
    model = Donor
    exclude = ("createdBy",)

class DonationForm(forms.ModelForm):
  class Meta:
    model = Donation
    exclude = ("donor",)
