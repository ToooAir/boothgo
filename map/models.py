from django.db import models
from django.conf import settings
import ast
from django.contrib.auth.models import User

from .storage import OverwriteStorage
#import周家豪寫的class
def Booth_file_name(instance, filename):
    return '/'.join(['Booth', instance.event.title + '_' + instance.number])
#上面兩行為booth的相片重新命名
def Event_file_name(instance, filename):
    return '/'.join(['Event', instance.title])
#上面兩行為event的相片重新命名

class Event(models.Model):
	title = models.CharField(max_length = 150)
	desc = models.CharField(max_length = 3000)
	event_date = models.CharField(max_length = 20)
	event_address = models.CharField(max_length = 150, null=True, default=None, blank=True)
	image = models.ImageField(upload_to=Event_file_name, storage= OverwriteStorage(), null=True, default=None)
	url = models.CharField(max_length = 150, null=True, blank=True)
	#修改image的上傳地點跟格式
	def __str__(self):
		return self.title


class Booth(models.Model):
	event = models.ForeignKey(Event,on_delete = models.CASCADE)
	number = models.CharField(max_length = 5, blank=True)
	group_name = models.CharField(max_length = 150, blank=True)
	desc = models.CharField(max_length = 1000, null=True, blank=True)
	works_type = models.CharField(max_length = 150, null=True, blank=True)
	works_tag = models.CharField(max_length = 150, null=True, blank=True)
	rl = models.CharField(max_length = 150, null=True, blank=True)
	image = models.ImageField(upload_to=Booth_file_name, storage= OverwriteStorage(), null=True, default=None, blank=True)
	#修改image的上傳地點跟格式
	def __str__(self):
		return self.number

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	image = models.ImageField(upload_to ='photos', null=True, default=None, blank=True)
	point = models.IntegerField(default=0)
	def __str__(self):
		return self.user.__str__()

class User_Favorite_Booth(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	booth = models.ForeignKey(Booth,on_delete = models.CASCADE, blank=True)
	def __str__(self):
		return '%s %s' %(self.user,self.booth)

class Comment(models.Model):
    content = models.CharField(max_length=1500)
    user = models.CharField(max_length=20)
    def __str__(self):
        return self.content