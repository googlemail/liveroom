#coding=utf-8
from django.db import models
from taggit.managers import TaggableManager
class Room(models.Model):
    nickname = models.CharField(max_length=70)
    username = models.CharField(max_length=70)
    gamename = models.CharField(max_length=50)
    status = models.CharField(max_length=70)
    tag = models.CharField(max_length=70)
    url = models.CharField(max_length=50,unique=True)
    img = models.CharField(max_length=170)
    sitename = models.CharField(max_length=70)
    renqi = models.FloatField()
    updatetime = models.CharField(max_length=50)
    tags = TaggableManager()
    def __str__(self):
        return self.url

class RoomTag(models.Model):
    tag = models.CharField(max_length=32,primary_key=True)
    roomroomtag = models.ManyToManyField(room)
    def __str__(self):
        return self.tag
class Food(models.Model):
    # ... fields here
    tags = TaggableManager()










# Create your models here.


##{url:[nickname,username,gamename,status,tag,url,img,sitename,renqi]}