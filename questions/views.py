from django.shortcuts import render
from questions.models import Question
from django.http import HttpResponse

def index(request):
  questions = Question.objects.all()
  #Does the first page of the questions
  if 'number' not in request.POST:
	context = {"questions": questions, "number": 1 }
	return render(request, "questions/index.html", context)
  else:
    number = int(request.POST['number'])
	
  #Getting the value for the answer	
  answer = int(request.POST[str(number)])
  
  # Number 1 is the first question for Donor Database
  if number == 1:
	if answer == 1:
	  generateDonorDatabase()
	  return HttpResponse("Generate Donor Database")
	else:
	  context = {"questions": questions, "number": 2 }
	  return render(request, "questions/index.html", context)
	  
  # Number 2 is the tracking data database
  elif number == 2 and answer == 1:
	  return HttpResponse("We have not finished this part! <br /> Work is still need.")
	
  return HttpResponse("We do not have the database you need!")

def generateDonorDatabase():
	return 0
  
def submit(request):
  questions = Question.objects.all()

  output = "<br />".join([request.POST[str(index.id)] for index in questions])
  for index in questions:
  	value = request.POST[str(index.id)]
  return HttpResponse(output)
