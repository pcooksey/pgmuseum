from django.db import models
from django.contrib.auth.models import User

class SiteName(models.Model):
  Code = models.CharField(max_length=2)
  Site_Name = models.CharField(max_length=50)
  
class ExplorationTime(models.Model):
  Start = models.TimeField()
  End = models.TimeField()
  Total = models.IntegerField()
  
class CountTime(models.Model):
  Start = models.TimeField()
  End = models.TimeField()
  Total = models.IntegerField()
  
class Observed(models.Model):
  Loners = models.IntegerField()
  Sunners = models.IntegerField()
  Fliers = models.IntegerField()
  Grounders = models.IntegerField()
  Dead = models.IntegerField()
  Mating = models.IntegerField()
  Total = models.IntegerField()
  
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

  SkyPercentage = models.IntegerField()
  BFT = models.IntegerField(max_length=1,choices=Beaufort_Scale_For_Sky, default=0)
  Precip = models.CharField(max_length=10,choices=PRECIP, default='none')
  Wind = models.IntegerField()
  WindDirection = models.TextField()
  Temp = models.IntegerField()

class Basic(models.Model):
  id = models.AutoField(primary_key = True)
  createdBy = models.ForeignKey(User)
  date = models.DateField()
  sitename = models.ForeignKey(SiteName)
  numerOfObservers = models.IntegerField()
  observers = models.TextField()
  exploration_time = models.OneToOneField(ExplorationTime)
  butterfliesOvserved = models.OneToOneField(Observed)
  weather = models.OneToOneField(Weather)
  count_time = models.OneToOneField(CountTime)
  
class ClusterInfo(models.Model):
  basic = models.ForeignKey(Basic)
  NumberClustered = models.IntegerField()
  NumberTagged = models.IntegerField()
  TreeSpecies = models.CharField(max_length=4)
  NumberOfTrees = models.IntegerField()
  Aspect = models.IntegerField()
  Height = models.IntegerField()