from django.db import models

class Question(models.Model):
  question = models.CharField(max_length = 200)
  
  def __unicode__(self):
	return self.question
	
#For now I am creating the Donor database model in here
class Donor(models.Model):
	firstName = models.CharField(max_length = 20)
	LastName = models.CharField(max_length = 20)
	email = models.EmailField()

class Donation(models.Model):
	account = models.ForeignKey(Donor)
	donation = models.DecimalField(max_digits=15, decimal_places=2)
	date = models.DateField(auto_now_add=True)
	