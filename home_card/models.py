from django.db import models

# Create your models here.
class home_card_1(models.Model):
    card_title = models.CharField(max_length=30,default= None,null = True)
    card_lng = models.CharField(max_length=30,default= None,null = True)
    card_author = models.CharField(max_length=30,default= None,null = True)
    card_pdate = models.IntegerField(default= None,null = True)
    card_desc = models.CharField(max_length=100,default= None,null = True)
    card_image = models.ImageField(upload_to="homecard1/",max_length=250, default=None, null=True)

class home_card_2(models.Model):
    card_title = models.CharField(max_length=30,default= None,null = True)
    card_lng = models.CharField(max_length=30,default= None,null = True)    
    card_author = models.CharField(max_length=30,default= None,null = True)
    card_pdate = models.IntegerField(default= None,null = True)
    card_desc = models.CharField(max_length=100,default= None,null = True)
    card_image = models.ImageField(upload_to="homecard1/",max_length=250, default=None, null=True)

class home_card_3(models.Model):
    card_title = models.CharField(max_length=30,default= None,null = True)
    card_lng = models.CharField(max_length=30,default= None,null = True)
    card_author = models.CharField(max_length=30,default= None,null = True)
    card_pdate = models.IntegerField(default= None,null = True)
    card_desc = models.CharField(max_length=100,default= None,null = True)
    card_image = models.ImageField(upload_to="homecard1/",max_length=250, default=None, null=True)

class home_card_4(models.Model):
    card_title = models.CharField(max_length=30,default= None,null = True)
    card_lng = models.CharField(max_length=30,default= None,null = True)
    card_author = models.CharField(max_length=30,default= None,null = True)
    card_pdate = models.IntegerField(default= None,null = True)
    card_desc = models.CharField(max_length=100,default= None,null = True)
    card_image = models.ImageField(upload_to="homecard1/",max_length=250, default=None, null=True)