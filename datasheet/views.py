from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datasheet.forms import BasicForm, ClusterForm
from datasheet.models import Basic, ClusterInfo

def index(request):
  if request.user.is_authenticated():
    
    #query_results = Donor.objects.all().filter(createdBy = request.user)

    basicForm = BasicForm()

    context = {"BasicForm": basicForm }

    if "error" in request.session:
      context["error"] = request.session["error"]
      del request.session["error"]

    return render(request, "datasheet/index.html", context)
  else:
    return redirect("/accounts/")