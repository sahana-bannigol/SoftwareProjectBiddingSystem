from django.db import models

# Create your models here
class Developer(models.Model) :
    dev_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100 )
    age = models.IntegerField()
    exp = models.TextField()
    cost = models.TextField()
    ph_no = models.CharField(max_length=10)
    service = models.TextField()
    email = models.TextField()
    pass_dev = models.TextField(default= None)
    dev_selected_flag = models.BooleanField(default=False)

class Client(models.Model) :
    client_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.TextField()
    ph_no = models.CharField(max_length=10)
    pass_client = models.TextField(default= None)

class Project(models.Model) :
    project_id = models.AutoField(primary_key= True)
    client_id=models.IntegerField(default=None)
    title = models.TextField()
    description = models.TextField()
    domain = models.TextField()
    lvl_exp = models.TextField()
    price_range = models.IntegerField()
    proj_selected_flag = models.BooleanField(default=False)

class PSRecord(models.Model) :
    bid_price = models.IntegerField()
    dev_id = models.IntegerField()
    dev_name=models.TextField(default=None)
    client_id = models.IntegerField()
    project_id = models.IntegerField()

class Final_bid(models.Model) :
    date = models.DateField(default= None)
    bid_price = models.IntegerField()
    dev_id = models.IntegerField()
    client_id = models.IntegerField()
    project_id = models.IntegerField()
    review = models.TextField()
    feedback = models.TextField()




