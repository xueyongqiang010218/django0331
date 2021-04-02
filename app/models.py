from django.db import models

# Create your models here.

class department(models.Model):
    dname = models.CharField(max_length=20)
    class Meta():
        db_table = "department"

class company(models.Model):
    cname = models.CharField(max_length=20)
    class Meta():
        db_table = "company"

class user(models.Model):
    username = models.CharField(max_length=20, null=False)
    number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    company_id=models.ForeignKey(company, on_delete=models.CASCADE)
    class Meta():
        db_table = "user"