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
		try:
			if accessCode:
				code = AccessCode.objects.get(Code = accessCode)
			else:
				return errorMessage(request, "Empty access code")
		except ObjectDoesNotExist:
			return errorMessage(request, "Invalid access code")

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

def logoutPage(request):
  logout(request)

  return redirect("/accounts/")

def home(request):
  if request.user.is_authenticated():
    return render(request, "accounts/home.html", {"user": request.user,})
  else:
    return redirect("/accounts/")
	
def export(request):
	if request.user.is_authenticated():
		# Create the HttpResponse object with the appropriate CSV header.
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="pgmuseumdatabase.csv"'

		# The data is hard-coded here, but you could load it from a database or
		# some other source.
		csv_data = [["Id","Date","Site Code","Site Name", "Number of Observers","Observers", "Exploration Start", "Exploration End", "Exploration Total", "Loners","Sunners","Fliers","Grounders","Dead","Mating","Total","Sky Percentage","BFT","Precip","Wind","Wind Direction", "Temperature","Count Start","Count End","Count Total","Water Source","Water Notes", "Nectar Source", "Nectar Notes", "Additional Notes","Bush Purple", "Butterfiles Eating", "Bush Yellow","Butterfiles Eating","Chaste Tree","Butterfiles Eating","Daisy Tree","Butterfiles Eating","Mallow Pink","Butterfiles Eating","Mallow Purple", "Butterfiles Eating","Goldenrod","Butterfiles Eating","Yellow Daisy","Butterfiles Eating","Bottlebrush Red","Butterfiles Eating", "Number clustered", "Number Tagged", "Tree species", "Number of Trees", "Aspect", "Height"]]
		basic = Basic.objects.all()
		clusters = ClusterInfo.objects.all() #.filter(basic = basic)
		for data in basic:
			list = []
			print data.id
			list.append(data.id)
			list.append(data.date)
			list.append(data.site_name.Code)
			list.append(data.site_name)
			list.append(data.number_of_observers)
			list.append(data.observers)
			list.append(data.exploration_time.start)
			list.append(data.exploration_time.end)
			list.append(data.exploration_time.total)
			list.append(data.butterflies_observed.loners)
			list.append(data.butterflies_observed.sunners)
			list.append(data.butterflies_observed.fliers)
			list.append(data.butterflies_observed.grounders)
			list.append(data.butterflies_observed.dead)
			list.append(data.butterflies_observed.mating)
			list.append(data.butterflies_observed.total)
			list.append(data.weather.skypercentage)
			list.append(data.weather.BFT)
			list.append(data.weather.precip)
			list.append(data.weather.wind)
			list.append(data.weather.winddirection)
			list.append(data.weather.temp)
			list.append(data.count_time.start)
			list.append(data.count_time.end)
			list.append(data.count_time.total)
			list.append(data.notes.waterSource)
			list.append(data.notes.waterNotes)
			list.append(data.notes.nectarSource)
			list.append(data.notes.nectarNotes)
			list.append(data.notes.additionalNotes)
			if data.site_name.Code == "PG":
				try:
					flowers = Flowers.objects.get(basic = data)
					list.append(flowers.butterfly_bush_purple)
					list.append(flowers.monarchs_eating_butterfly_bush_purple)
					list.append(flowers.butterfly_bush_yellow)
					list.append(flowers.monarchs_eating_butterfly_bush_yellow)
					list.append(flowers.chaste_tree)
					list.append(flowers.monarchs_eating_chaste_tree)
					list.append(flowers.daisy_tree)
					list.append(flowers.monarchs_eating_daisy_tree)
					list.append(flowers.mallow_pink)
					list.append(flowers.monarchs_eating_mallow_pink)
					list.append(flowers.mallow_purple)
					list.append(flowers.monarchs_eating_mallow_purple)
					list.append(flowers.goldenrod)
					list.append(flowers.monarchs_eating_goldenrod)
					list.append(flowers.yellow_daisy)
					list.append(flowers.monarchs_eating_yellow_daisy)
					list.append(flowers.bottlebrush_red)
					list.append(flowers.monarchs_eating_bottlebrush_red)
				except ObjectDoesNotExist:
					for num in range(0,15):
						list.append("N/A")
			else:
				for num in range(0,15):
					list.append("N/A")
					
			clusters = ClusterInfo.objects.all().filter(basic = data)
			for cluster in clusters:
				list.append(cluster.number_Clustered)
				list.append(cluster.number_tagged)
				list.append(cluster.tree_species)
				list.append(cluster.number_of_trees)
				list.append(cluster.aspect)
				list.append(cluster.height)
			
			csv_data.append(list)
			
		t = loader.get_template('accounts/database.txt')
		c = Context({
			'data': csv_data,
		})
		response.write(t.render(c))
		return response
	else:
		return redirect("/accounts/")