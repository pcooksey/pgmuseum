import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.models import AccessCode
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader, Context
from datasheet.models import *
from accounts.forms import *
from django.db.models import Count

def index(request):
  context = {}

  if request.user.is_authenticated():
    return redirect("home/")
  
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
		  return redirect("home/")
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
		accessCode = verifyPost(request, "accessCode")

		if email and password and firstName and lastName and password == confirmPassword:
			try:
				if accessCode:
					code = AccessCode.objects.get(Code = accessCode)
				else:
					return errorMessage(request, "Empty access code")
			except ObjectDoesNotExist:
				return errorMessage(request, "Invalid access code")
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
		if "code" in request.GET:
			code = request.GET["code"]
		else:
			code = 0
		return render(request, "accounts/register.html", {"code":code})

def errorMessage(request, error):
	email = verifyPost(request, "email")
	firstName = verifyPost(request, "firstName")
	lastName = verifyPost(request, "lastName")
	if "code" in request.GET:
		code = request.GET["code"]
	else:
		code = 0
	context = { "error": error, "code":code,"firstName":firstName,"lastName":lastName,"email":email }
	return render(request, "accounts/register.html", context)

def verifyPost(request, string):
  if string in request.POST:
    return request.POST[string]

  return ""

def logoutPage(request):
  logout(request)

  return redirect("/accounts/")

def home(request):
	if request.user.is_authenticated():
		if "start" not in request.GET:
			num = 0
		else:
			try:
				num = int(request.GET['start'])
			except ValueError:
				num = 0
			if num < 0:
				num = 0
		if request.user.is_staff:
			basics = Basic.objects.all().order_by('-date')[num:num+5]
		else:
			basics = Basic.objects.all().filter(createdBy = request.user).order_by('-date')[num:num+5]
		return render(request, "accounts/home.html", {"user": request.user, "basics":basics,"start":num})
	else:
		return redirect("/accounts/")
		
def extraInformation(request):
	if request.user.is_authenticated():
		if "id" in request.GET:
			clusters = ()
			flowers = ()
			if request.user.is_staff:
				try:
					basic = Basic.objects.get(id = request.GET["id"])
					clusters = ClusterInfo.objects.all().filter(basic = basic)
				except ObjectDoesNotExist:
					return HttpResponse("Does not exist")
			else:
				try:
					basic = Basic.objects.get(id = request.GET["id"], createdBy = request.user)
					clusters = ClusterInfo.objects.all().filter(basic = basic)
				except ObjectDoesNotExist:
					return HttpResponse("Does not exist")
			if basic.site_name.Code == "PG":
				try:
					flowers = Flowers.objects.all().filter(basic=basic)
				except ObjectDoesNotExist:
					flowers = ()
			return render(request, "accounts/extra.html", {"clusters": clusters, "flowers": flowers,})
		else:
			return HttpResponse("No ID for data collection")
	else:
		return redirect("/accounts/")
	
def export(request):
	if request.user.is_authenticated():
		# Create the HttpResponse object with the appropriate CSV header.
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="pgmuseumdatabase.csv"'

		# The data is hard-coded here, but you could load it from a database or
		# some other source.
		csv_data = [["ID","Date","Site Code","Site Name", "Number of Observers","Observers", "Exploration Start", "Exploration End", "Exploration Total", "Loners","Sunners","Fliers","Grounders","Dead","Mating","Total","Sky Percentage","BFT","Precip","Wind","Wind Direction", "Temperature","Count Start","Count End","Count Total","Water Source","Water Notes", "Nectar Source", "Nectar Notes", "Additional Notes",]]
		
		if request.method == 'POST':
			sites = request.POST.getlist('sites')
			basic = Basic.objects.filter(site_name__in=sites).order_by('site_name','-date')
		else:
			basic = Basic.objects.all().order_by('site_name','-date')
			
		for data in basic:
			grandTotal = 0
			list = []
			list.append(data.id)
			list.append(data.date)
			list.append(data.site_name.Code)
			list.append(data.site_name)
			list.append(data.number_of_observers)
			list.append(data.observers)
			list.append(data.exploration_time.start)
			list.append(data.exploration_time.end)
			list.append(data.exploration_time.exploration_total)
			list.append(data.butterflies_observed.loners)
			list.append(data.butterflies_observed.sunners)
			list.append(data.butterflies_observed.fliers)
			list.append(data.butterflies_observed.grounders)
			list.append(data.butterflies_observed.dead)
			list.append(data.butterflies_observed.mating)
			list.append(data.butterflies_observed.observed_total)
			list.append(data.weather.skypercentage)
			list.append(data.weather.BFT)
			list.append(data.weather.precip)
			list.append(data.weather.wind)
			list.append(data.weather.winddirection)
			list.append(data.weather.temp)
			list.append(data.count_time.count_start)
			list.append(data.count_time.count_end)
			list.append(data.count_time.count_total)
			list.append(data.notes.waterSource)
			list.append(data.notes.waterNotes)
			list.append(data.notes.nectarSource)
			list.append(data.notes.nectarNotes)
			list.append(data.notes.additionalNotes)
			csv_data.append(list)
			grandTotal += data.butterflies_observed.observed_total
			
			flowers = Flowers.objects.all().filter(basic = data)
			if data.site_name.Code == "PG" and flowers:
				list = ["","Flower","Eating"]
				csv_data.append(list)
				for flower in flowers:
					list = []
					list.append("")
					list.append(flower.flower)
					list.append(flower.eating)
					csv_data.append(list)
			
			clusters = ClusterInfo.objects.all().filter(basic = data)	
			if clusters:
				list = ["","Number Clustered", "Number Tagged", "Tree Species", "Number of Trees", "Height"]
				csv_data.append(list)
				for cluster in clusters:
					list = []
					list.append("")
					list.append(cluster.number_Clustered)
					list.append(cluster.tree_species)
					list.append(cluster.tree_ID)
					list.append(cluster.height)
					csv_data.append(list)
					grandTotal += cluster.number_Clustered
			else:
				list = ["","No Clusters Observed"]
				csv_data.append(list)
			list = ["", "Total Butterflies", grandTotal]
			csv_data.append(list)
		t = loader.get_template('accounts/database.txt')
		c = Context({
			'data': csv_data,
		})
		response.write(t.render(c))
		return response
	else:
		return redirect("/accounts/")
		
def delete(request):
  if request.user.is_authenticated():
    basic = Basic.objects.get(id = request.POST["delete"])

    if request.user.is_staff == True:
	  basic.delete()
 
    return redirect("/accounts/home/")
  else:
    return redirect("/accounts/")

def select(request):
  if request.user.is_authenticated():
	sites = SelectForm()
	return render(request, "accounts/select.html", {"sites":sites})
  else:
	return redirect("/accounts/")
	
def graph(request):
  if request.user.is_authenticated():
	basic = Basic.objects.values('site_name').annotate(count = Count('site_name'))
	return render(request, "accounts/graph.html", {"basics": basic})
  else:
	return redirect("/accounts/")