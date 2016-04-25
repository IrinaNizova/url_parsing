from django.db import models

class DataFromUrl(models.Model):
    url_id = models.IntegerField(blank=False)
    status_code = models.IntegerField()
    error_reason = models.CharField(max_length=100, default='OK')
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    charset = models.CharField(max_length=20)
    h1 = models.TextField()
