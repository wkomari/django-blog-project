from django.contrib import admin
from django.db import models

# Create your models here.

class Post(models.Model):
 title = models.CharField(max_length=60)
 body = models.TextField()
 date_created = models.DateField()
 date_updated = models.DateField()
 def __unicode__(self):
   return self.title

class Comment(models.Model):
 body = models.TextField()
 author = models.CharField(max_length=60)
 date_created = models.DateField()
 date_updated = models.DateField()
 web_post = models.ForeignKey(Post,related_name='web post') # one post to many comment
 def __unicode__(self):
  return self.author
admin.site.register(Post)
admin.site.register(Comment)
#admin.site.register(Blog)
