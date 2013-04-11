from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
  context = {}
  
  if "register" in request.POST:
    return redirect("/accounts/register/")
  elif "signin" in request.POST:
    if "email" in request.POST and "password" in request.POST:
      email = request.POST["email"]
      password = request.POST["password"]
      user = authenticate(username = email, password = password)

      if user is not None:
        if user.is_active:
          login(request, user)

          return redirect("/questions/")
        else:
          return render(request, "accounts/index.html", { "error": "Your account is disabled!" })
      else:
        return render(request, "accounts/index.html", { "error": "Incorrect username or password!" })
    else:
      return render(request, "accounts/index.html", { "error": "Incorrect username or password!" })
  else:
    return render(request, "accounts/index.html", context)

def register(request):
  if "createAccount" in request.POST:
  #Below should be refractored into a function to decrease code
    email = verifyPost(request, "email")
    password = verifyPost(request, "password")
    confirmPassword = verifyPost(request, "confirmPassword")
    firstName = verifyPost(request, "firstName")
    lastName = verifyPost(request, "lastName")

    if email and password and firstName and lastName and password == confirmPassword:
      object, created = User.objects.get_or_create(username = email)

      if created:
        object.email = email
        object.first_name = firstName
        object.last_name = lastName
        object.set_password(password)
        object.save()

        return redirect("/accounts/")
      else:
        return errorMessage(request, "User already exists!")
    elif password != confirmPassword:
      return errorMessage(request, "Your passwords do not match!")
    else:
      return errorMessage(request, "Please enter information in every field!")
  else:
    return render(request, "accounts/register.html", {})

def errorMessage(request, error):
  context = { "error": error }

  return render(request, "accounts/register.html", context)

def verifyPost(request, string):
  if string in request.POST:
    return request.POST[string]

  return ""
