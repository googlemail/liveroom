from django.db import models

class Question(models.Model):
    questiontext = models.CharField(max_length = 20)
    pubdate = models.DateField()
class Choice(models.Model):
    choicetext = models.CharField(max_length = 20)
    vote = models.IntegerField(default=0)
    tongbu = models.ForeignKey(Question)
class Yonghuming(models.Model):
    username = models.CharField(max_length=20)
    tongbu1 = models.ForeignKey(Question)
    def __str__(self):
        return self.username

class User(models.Model):
    pass
# Create your models here.
