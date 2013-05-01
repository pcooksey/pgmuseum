from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datasheet.forms import *
from datasheet.models import *

def index(request):
  if request.user.is_authenticated():
    
    #query_results = Donor.objects.all().filter(createdBy = request.user)

    basicForm = BasicForm()
	explorationForm = ExplorationForm()
	observedForm = ObservedForm()
	weatherForm = WeatherForm()
	countForm = CountForm()

    context = {
	  "BasicForm": basicForm, 
	  "ExplorationForm":explorationForm, 
	  "ObservedForm":observedForm,
	  "weatherForm":weatherForm,
	  "countForm":countForm,
	}

    if "error" in request.session:
      context["error"] = request.session["error"]
      del request.session["error"]

    return render(request, "datasheet/index.html", context)
  else:
    return redirect("/accounts/")