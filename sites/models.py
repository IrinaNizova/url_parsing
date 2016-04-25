# -*- coding: utf-8 -*-
from django.db import models
from datetime import timedelta, datetime, time
from .tasks import handling_url

class Sites(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    timeshift = models.TimeField(default=time(0, 0, 0))

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        super(Sites, self).save(*args, **kwargs)
        print(dir(self.timeshift))
        eta = datetime.now() + timedelta(hours=self.timeshift.hour,
                                         minutes=self.timeshift.minute,
                                         seconds=self.timeshift.second)
        handling_url.apply_async(args=[self.id, self.url], eta=eta)