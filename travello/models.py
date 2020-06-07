from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Destination(models.Model):

    country = models.CharField(max_length=100)
    #desc = models.TextField()
    total_cases = models.IntegerField()
    no_of_deaths = models.IntegerField()
    cases_cured = models.IntegerField()
    offer = models.BooleanField(default=False)

class Daily_cases(models.Model):
    
    iso_code = models.TextField(default=" ")
    location = models.TextField()
    date = models.TextField()
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    new_deaths = models.IntegerField()
    Graph_cases = models.TextField()

class people(models.Model):

    aadhaar_Id = models.IntegerField()
    name =  models.TextField(default=" ")
    phone_number = models.TextField(default=" ")
    age = models.IntegerField()
    address = models.TextField(default=" ")

class Travel_history(models.Model):
    person_id =models.TextField(default=" ")
    april_16 = models.TextField(default=" ")
    april_17 = models.TextField(default=" ")
    april_18 = models.TextField(default=" ")
    april_19 = models.TextField(default=" ")
    april_20 = models.TextField(default=" ")
    april_21 = models.TextField(default=" ")
    april_22 = models.TextField(default=" ")
    april_23 = models.TextField(default=" ")
    april_24 = models.TextField(default=" ")
    april_25 = models.TextField(default=" ")
    april_26 = models.TextField(default=" ")
    april_27 = models.TextField(default=" ")
    april_28 = models.TextField(default=" ")
    april_29 = models.TextField(default=" ")
    april_30 = models.TextField(default=" ")


class medical_history(models.Model):
    patient_id = models.TextField(default=" ")
    ischemic_heart_disease = models.TextField(default=" ")
    stroke = models.TextField(default=" ")
    bronchitis = models.TextField(default=" ")
    hiv_aids = models.TextField(default=" ")
    copd = models.TextField(default=" ")
    diabetes_mellitus = models.TextField(default=" ")
    cirrhosis = models.TextField(default=" ")
    kidney_disease = models.TextField(default=" ")

class quarantine_centres(models.Model):
    centre_name = models.TextField(default=" ")
    centre_id = models.TextField(default=" ")
    capacity = models.TextField(default=" ")
    address = models.TextField(default=" ")

class victims(models.Model):
    victim_id = models.TextField(default=" ")
    centre_id = models.TextField(default=" ")
    admit_date = models.TextField(default=" ")


class people3(models.Model):

    national_id = models.TextField(default=" ")
    name =  models.TextField(default=" ")
    phone_number = models.TextField(default=" ")
    age = models.IntegerField()
    address = models.TextField(default=" ")

class Travel_history2(models.Model):
    person_id =models.TextField(default=" ")
    april_16 = models.TextField(default=" ")
    april_17 = models.TextField(default=" ")
    april_18 = models.TextField(default=" ")
    april_19 = models.TextField(default=" ")
    april_20 = models.TextField(default=" ")
    april_21 = models.TextField(default=" ")
    april_22 = models.TextField(default=" ")
    april_23 = models.TextField(default=" ")
    april_24 = models.TextField(default=" ")
    april_25 = models.TextField(default=" ")
    april_26 = models.TextField(default=" ")
    april_27 = models.TextField(default=" ")
    april_28 = models.TextField(default=" ")
    april_29 = models.TextField(default=" ")
    april_30 = models.TextField(default=" ")

















