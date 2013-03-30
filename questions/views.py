from django.shortcuts import render
from questions.models import Question
from django.http import HttpResponse

def index(request):
  questions = Question.objects.all()
  context = {"questions": questions}

  return render(request, "questions/index.html", context)

def submit(request):
  questions = Question.objects.all()

  output = "<br />".join([request.POST[str(index.id)] for index in questions])

  return HttpResponse(output)
