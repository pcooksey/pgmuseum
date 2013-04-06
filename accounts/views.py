from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def index(request):
  context = {}

  return render(request, "accounts/index.html", context)

def register(request):
  context = {}

  return render(request, "accounts/register.html", context)
