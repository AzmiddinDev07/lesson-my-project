from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=221)
    content = models.TextField(blank=True, null=True)
    modifield_date = models.DateTimeField(auto_now=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)