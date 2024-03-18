from django.contrib import admin
from .models import UserProfile , Post , Comment, Story , Userdetails

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'followers_count', 'following_count')

    def followers_count(self, obj):
        return obj.followers.count()

    def following_count(self, obj):
        return obj.following.count()

    followers_count.short_description = 'Followers Count'
    following_count.short_description = 'Following Count'


class UserdetailsAdmin(admin.ModelAdmin):
    list_display = ("Profileimage",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("content", "image")    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text",)
class storyadmin(admin.ModelAdmin):
    list_display = ("contenttext","contentbackground","contentfstyle","storyfile")    
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post , PostAdmin)
admin.site.register(Comment , CommentAdmin)
admin.site.register(Story, storyadmin)
admin.site.register(Userdetails, UserdetailsAdmin)