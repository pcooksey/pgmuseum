from django.shortcuts import render, redirect
from questions.models import Question
from django.http import HttpResponse
from django import forms

def index(request):
  if request.user.is_authenticated(): 
    questions = Question.objects.all()
  
    # Does the first page of the questions
    if 'number' not in request.POST:
      context = { "questions": questions, "number": 1, "radio": True }
      return render(request, "questions/index.html", context)
    else:
      number = int(request.POST['number'])
  
    # Number 1 is the first question for Donor Database
    if number == 1: 
      answer = int(request.POST[str(number)])
      if answer == 1:
        generateDonorDatabase()
        return HttpResponse("Generating Donor Database")
      else:
        context = { "action": "", "questions": questions, "number": 2, "radio": True }
        return render(request, "questions/index.html", context)
    # Number 2 is the tracking data database
    elif number == 2:
      answer = int(request.POST[str(number)])

      if answer == 1:
        context = { "action": "", "questions": questions, "number": 3, "numberInput": True }
        return render(request, "questions/index.html", context)
    # Number 3 is getting the number of items in the database
    elif number == 3:
      if len(request.POST[str(number)]) == 0:
        context =  { "action": "", "questions": questions, "number": 3, "numberInput": True, "error": "You must have at least 1 item!" }
        return render(request, "questions/index.html", context)
    
      numOfFields = int(request.POST[str(number)])
      context = { "action": "inputs/", "number": 4, "numOfFields": range(numOfFields) }
      return render(request, "questions/index.html", context)

    return HttpResponse("We do not have the database you need!")
  else:
    return redirect("/accounts/")

def inputs(request):
  generateTrackingDatabase()
  return HttpResponse("Generating Tracking Database")

def generateDonorDatabase():
  return 0

def generateTrackingDatabase():
  return 0
