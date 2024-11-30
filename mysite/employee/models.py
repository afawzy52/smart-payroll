

from django.db import models

import uuid
from datetime import date
from .choices import Choices
from .models import dept, branch, designation, city

# Create your models here.
## employee class ------ ##
class emp(models.Model):
    dept_id = models.ForeignKey(dept, on_delete=models.CASCADE)
    emp_slug = models.UUIDField(default=uuid.uuid4, db_index=True)
    branch=models.ForeignKey(branch, on_delete=models.CASCADE)
    emp_id = models.AutoField(primary_key=True, blank=False)
    emp_fname = models.CharField(max_length=25)
    emp_lname= models.CharField(max_length=75)
    prefix = models.CharField(max_length=5, choices=Choices.prfix_title) # Mr.,Miss,Mrs
    dob = models.DateField()
    avatar = models.ImageField(blank=True, upload_to='emp_profile')
    hire_date = models.DateField(default=date.today)
    bank_id = models.IntegerField(null=True,blank=True)
    file_no = models.IntegerField(blank= True)
    job_title = models.ForeignKey(designation,blank= True,on_delete=models.CASCADE)
    marital_status = models.CharField(max_length= 15, choices=Choices.marital_state)
    mlitary_status = models.CharField(max_length=20, choices=Choices.military_state)
    address = models.CharField(max_length=250, blank=True)
    city_code = models.ForeignKey(city,on_delete=models.CASCADE)
    tel = models.IntegerField(blank=True)
    mobile = models.IntegerField(blank=True)
    id_no = models.IntegerField(blank=True)           # identification card No.
    bank_cash = models.BooleanField(blank=True, default=0)           # 0 for cash , 1 for bank
    bank_acc = models.IntegerField(blank=True)
    social_no = models.IntegerField(blank=True)        # social insurance No.
    social_ny = models.BooleanField(blank=True, default=0)                      # social insurance yes , no
    social_date = models.DateField(blank=True)
    social_insEmp = models.IntegerField(blank=True, default=0)   # calculate SoIns amount for emp
    social_insCom = models.IntegerField(blank=True, default=0)   # calculate SoIns amount for comp
    date_leave = models.DateField(blank=True)
    leave_for = models.CharField(max_length=25, choices=Choices.leave_for, blank=True)
    leave = models.BooleanField(blank=True, default=0)
    # class_id
    # title_grade
    # life_insurance
    # lifeInsdate
    # funds_amount
    # fundsy_n
    # funds_date
    # xwife_pay
    # wifepay_date
    education = models.CharField(max_length=50, blank=True)
    graduate_year = models.CharField(max_length=5, blank=True)
    graduate_from = models.CharField(max_length=50, blank=True)
    # qualification1
    # q1_date
    # qualification2
    # q2_date
    remarks = models.TextField(max_length=500, blank=True)
    