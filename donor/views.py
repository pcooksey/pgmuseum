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

def donations(request):
  if request.user.is_authenticated():
    if "donor" in request.POST:
	  request.session["donor"] = request.POST["donor"]
    elif "donor" not in request.session:
	  return redirect("/donor/")
	  
    donor = Donor.objects.get(id = request.session["donor"])
    query_results = Donation.objects.all().filter(donor = donor)

    donationForm = DonationForm()

    context = { "donations": query_results, "DonationForm": donationForm, "DonorId": request.session["donor"], "firstName": donor.firstName, "lastName": donor.lastName }

    if "error" in request.session:
      context["error"] = request.session["error"]
      del request.session["error"]

    return render(request, "donor/donations.html", context)
  else:
    return redirect("/accounts/")

def createNewDonation(request):
  if request.user.is_authenticated():
    donationForm = DonationForm(request.POST)

    if donationForm.is_valid():
      obj = donationForm.save(commit = False)
      obj.donor = Donor.objects.get(id = request.session["donor"])
      obj.save()

      return redirect("/donor/donations/")
    else:
      request.session["error"] = "Your input was invalid"
      return redirect("/donor/donations")
  else:
    return redirect("/accounts/")

def deleteDonation(request):
  if request.user.is_authenticated():
    donation = Donation.objects.get(id = request.POST["deleteDonation"])

    if donation.donor == Donor.objects.get(id = request.session["donor"]):
      donation.delete()
 
    return redirect("/donor/donations/")
  else:
    return redirect("/accounts/")
