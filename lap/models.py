from django.db import models

# Create your models here.
class Laptop(models.Model):
  name = models.CharField(max_length=255)
  sap_id = models.CharField(max_length=255)
  phone = models.CharField(max_length=255, null=True)
  laptop_brand = models.CharField(max_length=255,null=True)
  laptop_serial = models.CharField(max_length=255,null=True)
  laptop_age = models.IntegerField(null=True)
  motherboard_condition= models.CharField(max_length=255,null=True)
  display_condition= models.CharField(max_length=255,null=True)
  processor_age= models.CharField(max_length=255,null=True)
  speed = models.CharField(max_length=255,null=True)
  report_date = models.DateField(null=True)
  total_kpi_score = models.IntegerField(null=True)
  def __str__(self):
    return f"{self.name} {self.laptop_brand}"


class kpi(models.Model):
  type = models.CharField(max_length=255)
  match_string = models.CharField(max_length=255)
  kpi_score = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.type}:{self.match_string}={self.kpi_score}"


class repair(models.Model):
  name = models.CharField(max_length=255)
  sap_id = models.CharField(max_length=255)
  phone = models.CharField(max_length=255, null=True)
  laptop_brand = models.CharField(max_length=255,null=True)
  laptop_os = models.CharField(max_length=255,null=True)
  report_date = models.DateField(null=True)
  issue = models.TextField(null=True)
  urgency = models.CharField(max_length=255,null=True)


  def __str__(self):
    return f"{self.name}:{self.laptop_brand}={self.laptop_os}"