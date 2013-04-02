from django.shortcuts import render
from questions.models import Question
from django.http import HttpResponse
from django import forms

def index(request):
  questions = Question.objects.all()
  # Does the first page of the questions
  if 'number' not in request.POST:
    context = { "questions": questions, "number": 1, "radio": True }
    return render(request, "questions/index.html", context)
  else:
    number = int(request.POST['number'])
  
  # Getting the value for the answer 
  answer = int(request.POST[str(number)])
  
  # Number 1 is the first question for Donor Database
  if number == 1:
    if answer == 1:
      generateDonorDatabase()
      return HttpResponse("Generate Donor Database")
    else:
      context = { "questions": questions, "number": 2, "radio": True }
      return render(request, "questions/index.html", context)
  # Number 2 is the tracking data database
  elif number == 2 and answer == 1:
    context = { "questions": questions, "number": 3, "numberInput": True }
    return render(request, "questions/index.html", context)
  # Number 3 is getting the number of items in the database
  elif number == 3:
    numOfFields = int(request.POST[str(number)])
    context = { "number": 4, "numOfFields": range(numOfFields) }
    return render(request, "questions/index.html", context)
  # Number 4 is generating the tracking database
  elif number == 4:
    generateTrackingDatabase()

  return HttpResponse("We do not have the database you need!")

def generateDonorDatabase():
  return 0

def generateTrackingDatabase():
  return 0
