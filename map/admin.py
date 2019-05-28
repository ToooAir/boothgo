from django.contrib import admin
from .models import *

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'event_date','event_address','desc')
class BoothAdmin(admin.ModelAdmin):
    list_display = ('id','event', 'number','group_name','desc')
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'point')
class User_Favorite_BoothAdmin(admin.ModelAdmin):
    list_display = ('user', 'booth')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')

admin.site.register(Event,EventAdmin)
admin.site.register(Booth,BoothAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User_Favorite_Booth,User_Favorite_BoothAdmin)