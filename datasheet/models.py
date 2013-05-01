from django.db import models
from django.contrib.auth.models import User

class SiteName(models.Model):
  Code = models.CharField(max_length=2)
  site_name = models.CharField(max_length=50)
  
class ExplorationTime(models.Model):
  start = models.TimeField()
  end = models.TimeField()
  total = models.IntegerField()
  
class CountTime(models.Model):
  start = models.TimeField()
  end = models.TimeField()
  total = models.IntegerField()
  
class Observed(models.Model):
  loners = models.IntegerField()
  sunners = models.IntegerField()
  fliers = models.IntegerField()
  grounders = models.IntegerField()
  dead = models.IntegerField()
  mating = models.IntegerField()
  total = models.IntegerField()
  
class Weather(models.Model):
  Beaufort_Scale_For_Sky = (
	(0, 'Clear, few clouds'),
	(1, 'Partly cloudy, scattered'),
	(2, 'Mostly cloudy, broken'),
	(3, 'Overcast'),
	(4, 'Fog or smoke'),
	(5, 'Drizzle'),
	(6, 'Showers'),
  )
  PRECIP = (
    ('none','none'),
	('drizzle','drizzle'),
	('rain','rain'),
	('downpour','downpour'),
  )

  sky_percentage = models.IntegerField()
  BFT = models.IntegerField(max_length=1,choices=Beaufort_Scale_For_Sky, default=0)
  precip = models.CharField(max_length=10,choices=PRECIP, default='none')
  wind = models.IntegerField()
  wind_direction = models.TextField()
  temp = models.IntegerField()

class Basic(models.Model):
  id = models.AutoField(primary_key = True)
  createdBy = models.ForeignKey(User)
  date = models.DateField()
  site_name = models.ForeignKey(SiteName)
  number_of_observers = models.IntegerField()
  observers = models.TextField()
  exploration_time = models.OneToOneField(ExplorationTime)
  butterflies_observed = models.OneToOneField(Observed)
  weather = models.OneToOneField(Weather)
  count_time = models.OneToOneField(CountTime)
  
class ClusterInfo(models.Model):
  basic = models.ForeignKey(Basic)
  number_Clustered = models.IntegerField()
  number_tagged = models.IntegerField()
  tree_species = models.CharField(max_length=4)
  number_of_trees = models.IntegerField()
  aspect = models.IntegerField()
  height = models.IntegerField()