from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from datasheet.forms import *
from datasheet.models import *

def index(request):
	if request.user.is_authenticated():
		if request.method == 'POST' and 'new' not in request.POST:
			basicForm = BasicForm(request.POST)
			explorationForm = ExplorationForm(request.POST)
			observedForm = ObservedForm(request.POST)
			weatherForm = WeatherForm(request.POST)
			countForm = CountForm(request.POST)
			notesForm = NotesForm(request.POST)
			if basicForm.is_valid() and explorationForm.is_valid() and observedForm.is_valid() and weatherForm.is_valid() and countForm.is_valid() and notesForm.is_valid():
				basic = basicForm.save(commit = False)
				basic.createdBy = request.user
				basic.exploration_time = explorationForm.save()
				basic.butterflies_observed = observedForm.save()
				basic.weather = weatherForm.save()
				basic.count_time = countForm.save()
				basic.notes = notesForm.save()
				basic.save()
				return redirect('next/?id='+str(basic.id))
			else:
				context = {"BasicForm": basicForm,"ExplorationForm":explorationForm,"ObservedForm":observedForm,"WeatherForm":weatherForm,"CountForm":countForm,"NotesForm":notesForm,}
				return render(request, "datasheet/index.html", context)
		else:
			basicForm = BasicForm()
			explorationForm = ExplorationForm()
			observedForm = ObservedForm()
			weatherForm = WeatherForm()
			countForm = CountForm()
			notesForm = NotesForm()
			context = {"BasicForm": basicForm,"ExplorationForm":explorationForm,"ObservedForm":observedForm,"WeatherForm":weatherForm,"CountForm":countForm,"NotesForm":notesForm,}
		
			if "error" in request.session:
				context["error"] = request.session["error"]
				del request.session["error"]

			return render(request, "datasheet/index.html", context)
	else:
		return redirect("/accounts/")
		
def next(request):
	if request.user.is_authenticated() and 'id' in request.GET and 'done' not in request.GET:
		id = request.GET['id']
		try:
			basic = Basic.objects.get(createdBy = request.user, id=id)
			clusters = ClusterInfo.objects.all().filter(basic = basic)
			site = basic.site_name.Code
		except ObjectDoesNotExist:
			return redirect('/datasheet/')
		if site == 'PG':
			flowers = True
		else:
			flowers = False
		if request.method == 'GET':
			clusterForm = ClusterForm()
			context = {'clusters':clusters,'ClusterForm': clusterForm,'Flowers': flowers,'request':request,}
			return render(request, "datasheet/next.html", context)
		elif request.method == 'POST':
			clusterForm = ClusterForm(request.POST)
			if clusterForm.is_valid():
				cluster = clusterForm.save(commit = False)
				cluster.basic = basic
				cluster.save()
				clusterForm = ClusterForm()
			context = {'clusters':clusters,'ClusterForm': clusterForm,'Flowers': flowers,'request':request,}
			return render(request, "datasheet/next.html", context)	
	elif 'done' in request.GET and 'flower' in request.GET:
		return redirect('flowers/?id='+str(request.GET['id']))
	else:
		return redirect('/accounts/')
		
def flowers(request):
	if request.user.is_authenticated() and 'id' in request.GET:
		id = request.GET['id']
		try:
			basic = Basic.objects.get(createdBy = request.user, id=id)
			flowers = Flowers.objects.all().filter(basic = basic)
			site = basic.site_name.Code
		except ObjectDoesNotExist:
			return redirect('/datasheet/')
		if request.method == 'GET':
			flowerForm = FlowerForm()
			context = {'FlowerForm': flowerForm,'request':request,"flowers":flowers,}
			return render(request, "datasheet/next/flowers.html", context)
		elif request.method == 'POST':
			flowerForm = FlowerForm(request.POST)
			if flowerForm.is_valid():
				flower = flowerForm.save(commit = False)
				flower.basic = basic
				flower.save()
			context = {'FlowerForm': flowerForm,'request':request, "flowers":flowers,}
			return render(request, "datasheet/next/flowers.html", context)	
	else:
		return redirect('/accounts/')