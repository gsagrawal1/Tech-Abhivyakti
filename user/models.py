from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='following')
class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Profileimage = models.FileField(upload_to="profiles/",max_length=500, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, default=None, blank=True)
    image = models.FileField(upload_to="posts/",max_length=500, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenttext = models.TextField(null=True, default=None, blank=True)
    contentbackground = models.TextField(null = True, default=None, blank = True)
    contentfstyle = models.TextField(null = True, default=None, blank = True)
    storyfile = models.FileField(upload_to="stories/",max_length=500, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='stories')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"

