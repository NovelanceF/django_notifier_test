from django.db import models

class Post(models.Model):
    dog = models.CharField(max_length=200)
    post_date = models.DateTimeField("date published")
    body = models.CharField(max_length=500)

    def __unicode__(self):
        return self.dog