from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def index(request):
  context = {"number": "1"}

  return render(request, "accounts/index.html", context)
