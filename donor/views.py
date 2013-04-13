from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from donor.forms import DonorForm, DonationForm
from donor.models import Donor, Donation

def index(request):
  if request.user.is_authenticated():
    # Only show the User's Donor database
    query_results = Donor.objects.all().filter(createdBy = request.user)

    donorForm = DonorForm()

    context = { "donors": query_results, "DonorForm": donorForm }

    if "error" in request.session:
      context["error"] = request.session["error"]
      del request.session["error"]

    return render(request, "donor/index.html", context)
  else:
    return redirect("/accounts/")
 
def createNewDonor(request):
  if request.user.is_authenticated():
    donorForm = DonorForm(request.POST)

    if donorForm.is_valid():
      obj = donorForm.save(commit = False)
      obj.createdBy = request.user
      obj.save()

      return redirect("/donor/")
    else:
      request.session["error"] = "Your input was invalid"
      return redirect("/donor/")
  else:
    return redirect("/accounts/")

def deleteDonor(request):
  if request.user.is_authenticated():
    donor = Donor.objects.get(id = request.POST["deleteDonor"])

    if donor.createdBy == request.user:
      donor.delete()
 
    return redirect("/donor/")
  else:
    return redirect("/accounts/")
