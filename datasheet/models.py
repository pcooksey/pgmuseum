from django.db import models
from django.contrib.auth.models import User

class SiteName(models.Model):
  Code = models.CharField(max_length=2)
  site_name = models.CharField(max_length=50)
  
  def __unicode__(self):
    return self.site_name

class TreeSpecie(models.Model):
  Code = models.CharField(max_length=5)
  tree_name = models.CharField(max_length=100)
  
  def __unicode__(self):
    return self.tree_name
	
class FlowerSpecie(models.Model):
  flower_name = models.CharField(max_length=100)
  
  def __unicode__(self):
    return self.flower_name
  
class ExplorationTime(models.Model):
  start = models.TimeField()
  end = models.TimeField()
  exploration_total = models.IntegerField()
  
class CountTime(models.Model):
  start = models.TimeField()
  end = models.TimeField()
  count_total = models.IntegerField()
  
class Observed(models.Model):
  loners = models.IntegerField()
  sunners = models.IntegerField()
  fliers = models.IntegerField()
  grounders = models.IntegerField()
  dead = models.IntegerField()
  mating = models.IntegerField()
  observed_total = models.IntegerField()
  
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
  PRECENTAGE = (
    ('0-25%','0-25%'),
	('26-50%','26-50%'),
	('51-75%','51-75%'),
	('76-100%','76-100%'),
  )
  
  skypercentage = models.CharField(max_length=10,choices=PRECENTAGE, default='0-25%')
  BFT = models.IntegerField(max_length=1,choices=Beaufort_Scale_For_Sky, default=0)
  precip = models.CharField(max_length=10,choices=PRECIP, default='none')
  wind = models.DecimalField(max_digits=5, decimal_places=2)
  winddirection = models.CharField(max_length=20)
  temp = models.DecimalField(max_digits=5, decimal_places=2)
  
class Note(models.Model):
  ANSWER = (
    ('No','No'),
	('Yes','Yes'),
  )
  waterSource = models.CharField(max_length=3, choices=ANSWER, default='No')
  waterNotes = models.CharField(max_length=150)
  nectarSource = models.CharField(max_length=3, choices=ANSWER, default='No')
  nectarNotes = models.CharField(max_length=150)
  additionalNotes = models.CharField(max_length=250)
  
class Basic(models.Model):
  id = models.AutoField(primary_key = True)
  createdBy = models.ForeignKey(User)
  date = models.DateField()
  site_name = models.ForeignKey(SiteName)
  number_of_observers = models.IntegerField()
  observers = models.CharField(max_length=100)
  exploration_time = models.OneToOneField(ExplorationTime)
  butterflies_observed = models.OneToOneField(Observed)
  weather = models.OneToOneField(Weather)
  count_time = models.OneToOneField(CountTime)
  notes = models.OneToOneField(Note)
  
  def delete(self, *args, **kwargs):
	self.exploration_time.delete()
	self.butterflies_observed.delete()
	self.weather.delete()
	self.count_time.delete()
	self.notes.delete()
	return super(self.__class__, self).delete(*args, **kwargs)
  
class ClusterInfo(models.Model):
  id = models.AutoField(primary_key = True)
  basic = models.ForeignKey(Basic)
  number_Clustered = models.IntegerField()
  number_tagged = models.IntegerField()
  tree_species = models.ForeignKey(TreeSpecie)
  tree_ID = models.CharField(max_length=20)
  height = models.DecimalField(max_digits=5, decimal_places=2)
  
class Flowers(models.Model):
  id = models.AutoField(primary_key = True)
  basic = models.ForeignKey(Basic)
  flower = models.ForeignKey(FlowerSpecie)
  eating = models.IntegerField()